'''
5.21

'''
import math
import random
import numpy as np
import networkx as nx
from datetime import date
from utils import load_my_graph, time2int, alias_setup, alias_draw


class graphSys:
    def __init__(self, graph, studentN, teacherN, nHighThresh=30):
        self.graph = graph
        self.studentNum = studentN
        self.teacherNum = teacherN
        self.nHighThresh = nHighThresh
        self.nHighVisit = 0
        self.nHighSet = set()
        self.alias_nodes = None
        self.get_alias_nodes()

    def get_alias_node(self, node):
        assert node < 0, 'only student node needs to get processed'
        unnormalized_probs = [self.graph.degree[nbr] for nbr in sorted(self.graph.neighbors(node))]
        norm_const = sum(unnormalized_probs)
        normalized_probs = [prob / norm_const for prob in unnormalized_probs]
        self.alias_nodes[node] = alias_setup(normalized_probs)

    def get_alias_nodes(self):
        alias_nodes = {}
        for node in self.graph.nodes:
            if node < 0:  # student node
                unnormalized_probs = [self.graph.degree[nbr] for nbr in sorted(self.graph.neighbors(node))]
                norm_const = sum(unnormalized_probs)
                normalized_probs = [prob / norm_const for prob in unnormalized_probs]
                alias_nodes[node] = alias_setup(normalized_probs)
        self.alias_nodes = alias_nodes

    def sampleWalkLength(self, alpha):
        return 10

    def getWeightedNb(self, node):
        neighbors = sorted(self.graph.neighbors(node))
        # print(f'node:{node}, alias_nodes:{self.alias_nodes[node]}')
        return neighbors[alias_draw(self.alias_nodes[node][0], self.alias_nodes[node][1])]

    def getNb(self, node):
        neighbors = [n for n in self.graph[node]]
        return random.choice(neighbors)

    def addNode(self, nodeType):
        '''
        add a new node, the node id should be assigned by the system
        nodeType should be 'student' or 'professor'\'teacher'
        :return: new node id
        '''
        if nodeType == 'student':
            self.studentNum += 1
            self.graph.add_node(-self.studentNum)
            return -self.studentNum
        elif nodeType == 'professor' or nodeType == 'teacher':
            self.teacherNum += 1
            self.graph.add_node(self.teacherNum)
            return self.teacherNum
        else:
            raise ValueError('Unexpected node type. Only \'student\',\'teacher\' and \'professor\' are accepted. ')

    def checkValidNode(self, nodeId):
        if nodeId < 0:
            return nodeId >= -self.studentNum
        elif nodeId > 0:
            return nodeId <= self.teacherNum
        return False

    def addEdge(self, src, tgt):
        if src * tgt >= 0:
            raise ValueError('Must be one student and one teacher.')
        if self.checkValidNode(src) and self.checkValidNode(tgt):
            self.graph.add_edge(src, tgt,weight=date.today().strftime('%Y-%m-%d'))
            if src > 0:
                for node in self.graph.neighbors(src):
                    self.get_alias_node(node)
            else:
                for node in self.graph.neighbors(tgt):
                    self.get_alias_node(node)
        else:
            raise ValueError(f'Given node ID should be between [-{self.studentNum},-1] or '
                             f'[1,{self.teacherNum}]')

    def pixieRandomWalk(self, query, alpha, N, nHigh=8, high=4):
        '''

        :param query: int, node id, must be teacher's node
        :param alpha: float, a parameter that determines walk length
        :param N: int,max total steps
        :param nHigh: int, max number of high visited nodes
        :param high: int, criteria of high visit
        :return: dict, key: int, node id, val: int, visit counts
        '''
        totSteps = 0
        nHighVisit = 0
        visitTime = dict()
        assert query > 0, 'Teacher node expected, got student'
        while totSteps < N and self.nHighVisit < self.nHighThresh and nHighVisit < nHigh:
            currPin = query
            currSteps = self.sampleWalkLength(alpha)
            for i in range(currSteps):
                oneHopNb = self.getNb(currPin)
                currPin = self.getWeightedNb(oneHopNb)
                visitTime[currPin] = visitTime.get(currPin, 0) + 1
                if visitTime[currPin] == high:
                    print(f'high node:{currPin}')
                    nHighVisit += 1
                    if currPin not in self.nHighSet:
                        self.nHighVisit += 1
                        self.nHighSet.add(currPin)
            totSteps += currSteps
        return visitTime

    def singleRecommend(self, query, alpha, N, nHigh=10):
        '''
        single teacher node query, no repetition
        #TODO:teachers with similar interests should be preferred
        :param query: teacher node, >0
        :param alpha:
        :param N: total steps
        :param nHigh: stop after nHigh teachers are frequently visited
        :return:
        '''
        assert query > 0
        self.nHighVisit = 0
        self.nHighSet.clear()
        visit = self.pixieRandomWalk(query, alpha, N, nHigh=nHigh)
        pairList = []
        for node in visit:
            if node != query:
                pairList.append([visit[node], node])
        pairList.sort(reverse=True)
        return pairList

    def userRecommend(self, query, N=140):
        '''
        student recommend
        :param query: student node,<0
        :param alpha:
        :param N: total steps
        :param nHigh: stop after nHigh teachers are frequently visited
        :return:
        '''
        assert query < 0
        self.nHighVisit = 0
        self.nHighSet.clear()

        queries, weights = [], []
        for nb in self.graph.neighbors(query):
            queries.append(nb)
            weights.append(time2int(self.graph[query][nb]['weight']))
        weightSum = sum(weights)
        normalizedWeights = [x / weightSum for x in weights]
        return self.pixieRecommend(queries,  normalizedWeights, N)

    def pixieRecommend(self, queries, weights, N, alpha=1):
        '''

        :param queries: list, list of query pins
        :param weights: list, list of weights for each query, must have equal length to queries
        :param alpha: float, a parameter that determines walk length
        :param N: int,determine max total steps
        :return:list<list<int,len=2>>,for each nested list element, element[0]=score, element[1]=id
        '''
        self.nHighVisit = 0
        self.nHighSet.clear()

        score = np.zeros(len(queries))
        visitTime = dict()
        for i, query in enumerate(queries):
            nbCnt = self.graph.degree[query]
            score[i] = nbCnt
        score /= np.sum(score)

        weight_incr_order = np.argsort(weights)

        for i in range(len(queries) - 1, -1, -1):  # start from node with higher weight
            ind = weight_incr_order[i]
            totSteps = score[ind] * weights[ind] * N
            print(f'node:{queries[ind]}')
            visit = self.pixieRandomWalk(queries[ind], alpha, totSteps, nHigh=max(10 - 5 * i, 3))
            for node in visit:
                visitTime[node] = visitTime.get(node, 0) + math.sqrt(visit[node])
        pairList = []
        for node in visitTime:
            pairList.append([visitTime[node] ** 2, node])
        pairList.sort(reverse=True)
        return pairList

    def getNeighborInfo(self,node):
        assert (node>=1 and node<=numTeachers) or (node<=-1 and node>=-numStudents)
        pairList=[]
        for nb in self.graph.neighbors(node):
            pairList.append([time2int(self.graph[nb][node]['weight']),nb])
        pairList.sort(reverse=True)
        return pairList


if __name__ == '__main__':
    '''load graph'''
    # graph_path = 'rnd_bipartite_2.txt'
    # myGraph, numStudents, numTeachers = load_my_graph(graph_path, verbose=True)
    # mySys=graphSys(myGraph,numStudents,numTeachers)

    myGraph=nx.Graph()
    myGraph.add_nodes_from([1, 2, 3, 4, -1])
    myGraph.add_edge(-1, 1)
    numStudents, numTeachers = 1, 4

    mySys = graphSys(myGraph, numStudents, numTeachers)

    mySys.addEdge(-1, 3)
    mySys.addNode('student')
    mySys.addNode('teacher')
    mySys.addEdge(-1,  5)
    mySys.addEdge(-2, 3)
    mySys.addEdge(-2, 4)

    query = [3, 1]  # 老师
    weight = [1/2, 1/2]
    visitTime = mySys.pixieRecommend(query, weight, 20)
    print(visitTime)
    alpha = 1
    visitTime = mySys.singleRecommend(5, alpha, 4)
    print(visitTime)


    # student=-5
    # nbInfo=mySys.getNeighborInfo(student)
    # print(nbInfo)
    # visitTime = mySys.userRecommend(student)
    # print(visitTime)

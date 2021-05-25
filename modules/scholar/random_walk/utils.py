import networkx as nx
from networkx.algorithms import bipartite
import pandas as pd
import numpy as np


def load_my_graph(graph_path, verbose=False):
    df = pd.read_csv(graph_path, delimiter=',')
    headers = list(df.columns)
    num_teachers, num_students = int(headers[0]), int(headers[1])

    myGraph = nx.Graph()
    myGraph.add_nodes_from([i + 1 for i in range(num_teachers)], bipartite=0)
    myGraph.add_nodes_from([-(i + 1) for i in range(num_students)], bipartite=1)

    edge_list = [[row[headers[0]], row[headers[1]], {'weight': row[headers[2]] }] for _, row in df.iterrows()]
    myGraph.add_edges_from(edge_list)

    # for edge in myGraph.edges.data():
    #     print(edge)

    if verbose:
        print(f'number of nodes:{myGraph.number_of_nodes()},{num_teachers} teachers, {num_students} students')
        print(f'number of edges:{myGraph.number_of_edges()}')
    return myGraph,num_students,num_teachers


def time2int(date):
    '''
    :return: number of days from 2020-01-01
    '''
    date_li = list(map(int, date.split('-')))
    days = (date_li[0] - 2020) * 365 + (date_li[1] - 1) * 30 + date_li[2] - 1
    return days


def alias_setup(probs):
    '''
    Compute utility lists for non-uniform sampling from discrete distributions.
    Refer to https://hips.seas.harvard.edu/blog/2013/03/03/the-alias-method-efficient-sampling-with-many-discrete-outcomes/
    for details
    '''
    K = len(probs)
    q = [0 for _ in range(K)]
    J = [0 for _ in range(K)]

    smaller = []
    larger = []
    for kk, prob in enumerate(probs):
        q[kk] = K * prob
        if q[kk] < 1.0:
            smaller.append(kk)
        else:
            larger.append(kk)

    while len(smaller) > 0 and len(larger) > 0:
        small = smaller.pop()
        large = larger.pop()

        J[small] = large
        q[large] = q[large] + q[small] - 1.0
        if q[large] < 1.0:
            smaller.append(large)
        else:
            larger.append(large)

    return J, q

def alias_draw(J, q):
    '''
    Draw sample from a non-uniform discrete distribution using alias sampling.
    '''
    K = len(J)

    kk = int(np.floor(np.random.rand() * K))
    if np.random.rand() < q[kk]:
        return kk
    else:
        return J[kk]

def load_my_graph_2(graph_path, verbose=False):
    '''
    :param graph_path:
    :return: nx Graph, bipartite
    '''
    df = pd.read_csv(graph_path, delimiter=',')
    headers = list(map(int, list(df.columns)))
    num_teachers, num_students = headers[0], headers[1]
    myGraph = nx.Graph()
    myGraph.add_nodes_from([i + 1 for i in range(num_teachers)], bipartite=0)
    myGraph.add_nodes_from([-(i + 1) for i in range(num_students)], bipartite=1)

    edge_list = [[row[0], row[1]] for row in df[list(df.columns)].to_numpy()]
    myGraph.add_edges_from(edge_list)
    if verbose:
        print(f'number of nodes:{myGraph.number_of_nodes()},{num_teachers} teachers, {num_students} students')
        print(f'number of edges:{myGraph.number_of_edges()}')
    return myGraph


if __name__ == '__main__':
    # graph_path = 'rnd_bipartite_2.txt'
    # graph,student_num,teacher_num = load_my_graph(graph_path)
    # print(graph.degree[-1])
    pass


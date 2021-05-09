from elasticsearch import Elasticsearch

es = Elasticsearch()


def create_index():
    mapping = {
        'properties': {
            'tid': {
                'type': 'integer',
                'index': 'true',
            },
            'name': {
                'type': 'keyword'
            },
            'category': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            },
            'paper': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            },
        }
    }
    es.indices.delete(index='scholar', ignore=[400, 404])
    es.indices.create(index='scholar', ignore=400)
    result = es.indices.put_mapping(index='scholar', doc_type='teacherInfo', body=mapping)
    print(result)


def insert_data():
    datas = [
        {
            'tid': 1,
            'name': '张拳石',
            'category': '机器学习 可解释性',
            'paper': '学习硬知识 公务员狗都不去 这辈子也就那样了'
        },
        # {
        #     'tid': 2,
        #     'name': '高晓沨',
        #     'category': '数学建模',
        #     'paper': '软知识 美赛'
        # },
        # {
        #     'tid': 3,
        #     'name': '蒋力',
        #     'category': '操作系统',
        #     'paper': '试试搜索 公务员'
        # },
        # {
        #     'tid': 4,
        #     'name': '周军',
        #     'category': '计算机视觉',
        #     'paper': '不知道了'
        # },
    ]

    # datas = [
    #     {
    #         'tid': 5,
    #         'name': '张伟楠',
    #         'category': '机器学习 强化学习',
    #         'paper': '这里还是公务员 为什么这么多公务员'
    #     },
    #     {
    #         'tid': 6,
    #         'name': '王新兵',
    #         'category': 'Ace map',
    #         'paper': '王新兵也用公务员'
    #     },
    # ]

    for data in datas:
        result = es.index(index='scholar', doc_type='teacherInfo', body=data)
        print(result)


def delete_data():
    result = es.delete(index='scholar', doc_type='teacherInfo', id='G24-UXkBgmYcnUKAtl0d')
    print(result)
    # result = es.delete(index='scholar', doc_type='teacherInfo', id='7iboSnkBope82AWuUSx2')
    # print(result)


def query_data():
    query = {
        "query": {
            "query_string": {
                "default_field": "paper",
                "query": "公务员狗"
            }
        }
    }
    result = es.search(index='scholar', doc_type='teacherInfo', body=query)
    for k, v in result['hits']['hits'][0].items():
        print(k, v)
    for k, v in result['hits']['hits'][1].items():
        print(k, v)
    # print(result)


if __name__ == '__main__':
    # insert_data()
    pass
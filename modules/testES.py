from elasticsearch import Elasticsearch
import pickle

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
            'avatar': {
                'type': 'keyword'
            },
            'title': {
                'type': 'keyword'
            },
            'school': {
                'type': 'keyword'
            },
            'heat': {
                'type': 'integer',
            },
            'all_field': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index='scholar', ignore=[400, 404])
    es.indices.create(index='scholar', ignore=400)
    result = es.indices.put_mapping(index='scholar', doc_type='teacherInfo', body=mapping)
    print(result)


def delete_index():
    res = es.indices.delete('scholar', ignore=[400, 404])
    print(res)


def insert_data():
    f = open("scholar/random_walk/es_data2", "rb")
    datas = pickle.load(f)
    f.close()
    # cnt = 0
    # for i in datas:
    #     if i['all_field'] != "":
    #         cnt += 1
    # print(len(datas), cnt)
    # exit(0)
    # for data in datas:
    #     result = es.index(index='scholar', doc_type='teacherInfo', body=data)
    #     print(result)
    # exit(0)
    # datas = [
    #     {
    #         'tid': 1,
    #         'name': 'Quanshi Zhang',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 1,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 2,
    #         'name': 'Xiaofeng Gao',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 2,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 3,
    #         'name': 'Cewu Lu',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 3,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 4,
    #         'name': 'Xinbing Wang',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 4,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 5,
    #         'name': 'Kai Yu',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 5,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 6,
    #         'name': 'Yong Yu',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 6,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 7,
    #         'name': 'Haiming Jin',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 7,
    #         'paper': 'Improving PPSZ for 3-SAT using critical variablesT Hertli',
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    #     {
    #         'tid': 8,
    #         'name': 'Liyao Xiang',
    #         'avatar': 'http://qszhang.com/files/photo.png',
    #         'title': 'Associate professor',
    #         'school': 'Shanghai Jiao Tong University',
    #         'heat': 8,
    #         'paper': "200932Improving PPSZ for 3-SAT using critical variablesT Hertli",
    #         'all_field': 'Improving PPSZ for 3-SAT using critical variablesT Hertli'
    #     },
    # ]
    # datas = [
    #     {
    #         'tid': 1,
    #         'name': '?????????',
    #         'category': '???????????? ????????????',
    #         'paper': '??????????????? ????????????????????? ????????????????????????'
    #     },
    #     {
    #         'tid': 2,
    #         'name': '?????????',
    #         'category': '????????????',
    #         'paper': '????????? ??????'
    #     },
    #     {
    #         'tid': 3,
    #         'name': '??????',
    #         'category': '????????????',
    #         'paper': '???????????? ?????????'
    #     },
    #     {
    #         'tid': 4,
    #         'name': '??????',
    #         'category': '???????????????',
    #         'paper': '????????????'
    #     },
    #     {
    #         'tid': 5,
    #         'name': '?????????',
    #         'category': '???????????? ????????????',
    #         'paper': '????????????????????? ???????????????????????????'
    #     },
    #     {
    #         'tid': 6,
    #         'name': '?????????',
    #         'category': 'Ace map',
    #         'paper': '????????????????????????'
    #     },
    # ]

    # datas = [
    #     {
    #         'tid': 5,
    #         'name': '?????????',
    #         'category': '???????????? ????????????',
    #         'paper': '????????????????????? ???????????????????????????'
    #     },
    #     {
    #         'tid': 6,
    #         'name': '?????????',
    #         'category': 'Ace map',
    #         'paper': '????????????????????????'
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
                "query": "????????????"
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
    # delete_index()
    # create_index()
    insert_data()

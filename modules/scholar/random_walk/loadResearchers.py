import pickle
import io
import sys
import random
import json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
f = open("researchers", "rb")
data = pickle.load(f)
f.close()
print(len(data))
print(data[0].keys())
# exit(0)
cnt = 0
es_data = []

teacher_name = ["Fan Cheng", "Junchi Yan", "Quanshi Zhang", "Xinbing Wang", "Xiaofeng Gao", "Yong Yu", "Luoyi Fu", "Yaohui Jin"]

for id, people in enumerate(data):
    people_data = {}
    people_data["tid"] = people["ID"]
    people_data["name"] = people["Name"]
    people_data["avatar"] = people["Avatar"]
    people_data["title"] = people["Title"]
    people_data["school"] = people["University"]
    if people["Name"] in teacher_name:
        people_data["heat"] = random.randint(50, 100)
    else:
        people_data["heat"] = random.randint(10, 40)

    all_type = people["Name"] + " "
    # print()
    tmp = people["Mottos"]
    tmp = eval(tmp)
    if tmp is not None:
        people["Mottos"] = tmp["Mottos"]
    else:
        people["Mottos"] = []
    print(type(people["Mottos"]), people["Mottos"])
    # print(type(tmp), tmp)
    print(type(people["ResearchInterest"]), people["ResearchInterest"])
    for item in people["ResearchInterest"]:
        all_type += item
        all_type += " "
    tmp = people["Awards"]
    tmp = eval(tmp)
    if tmp is not None:
        people["Awards"] = tmp["Awards"]
    else:
        people["Awards"] = []
    print(type(people["Awards"]), people["Awards"])
    if people["Papers"] is None:
        people["Papers"] = []
    print(type(people["Papers"]), people["Papers"])

    for item in people["Papers"]:
        all_type += item["Paper_name"]
        all_type += " "

    tmp = people["Cited_graph"]
    # print(tmp)
    if tmp is None:
        people["Cited_graph"] = []
    # # tmp = eval(tmp)
    # if tmp is not None:
    #     people["Cited_graph"] = tmp["Cited_graph"]
    # else:
    #     people["Cited_graph"] = []
    print(type(people["Cited_graph"]), people["Cited_graph"])
    tmp = people["Co_authors"]
    # print(tmp)
    if tmp is None:
        people["Co_authors"] = []
    # print(tmp)
    # tmp = eval(tmp)
    # if tmp is not None:
    #     tmp = eval(tmp)
    #     people["Co_authors"] = tmp["Co_authors"]
    # else:
    #     people["Co_authors"] = []
    print(type(people["Co_authors"]), people["Co_authors"])
    people_data["all_field"] = all_type
    es_data.append(people_data)
    # print(people["Co_authors"])
    print()
print(cnt)

for i in es_data:
    print(i)

f = open("es_data", "wb")
pickle.dump(es_data, f)
f.close()
import os
import json
import pymysql

def get_files(path='./data/features', rule=".json"):
    all = []
    for fpathe,dirs,fs in os.walk(path):   # os.walk是获取所有的目录
        for f in fs:
            filename = os.path.join(fpathe,f)
            if filename.endswith(rule):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all


# return [{}, {}]
def load_json(filename):
    with open(filename, 'r', encoding="utf8") as load_f:
        load_dict = json.load(load_f)
        return load_dict["features"]


def find_Co_authors(name, google_data):
    for data in google_data:
        if name == data["Name"]:
            return data["Co_authors"]


def find_Papers(name, google_data):
    for data in google_data:
        if name == data["Name"]:
            return data["Papers"]

def find_Cited_graph(name, google_data):
    for data in google_data:
        if name == data["Name"]:
            return data["Cited_graph"]


def data_for_db(researchers, google_data):
    data = []
    print("len(researcher)", researchers[0])
    for ID, researcher in enumerate(researchers):
        Co_authors = find_Co_authors(researcher['Name'], google_data)
        Papers = find_Papers(researcher['Name'], google_data)
        Cited_graph = find_Cited_graph(researcher['Name'], google_data)
        print("researcher", researcher['Name'])
        if not "Lab" in researcher.keys():
            researcher["Lab"] = "John Hopcroft Center for Computer Science"
        if not "ResearchInterest" in researcher.keys():
            researcher["ResearchInterest"] = ['cloud computing', 'distributed computation', 'machine learning', 'AI']
        print(researcher['ResearchInterest'])
        data.append({
            'ID': ID,
            'Name': researcher['Name'],
            'Avatar': researcher['Avatar'],
            'Title': researcher['Title'],
            'HomePage': researcher['HomePage'],
            'University': researcher['University'],
            'Lab': researcher["Lab"],
            'Bio': "Before he joined SJTU, he was a research fellow at Stanford University working under Prof. Fei-Fei Li and Prof. Leonidas J. Guibas. He was a Research Assistant Professor at Hong Kong University of Science and Technology with Prof. Chi Keung Tang . He got the his PhD degree from The Chinese Univeristy of Hong Kong, supervised by Prof. Jiaya Jia. He is one of core technique member in Stanford-Toyota autonomous car project (斯坦福-丰田，无人车项目). Some of his proposed algorithms have been used as a basic tool function in OpenCV(such as decolor.cpp). He has one Best Paper Award at the Non-Photorealistic Animation and Rendering (NPAR) 2012 and one most cited paper among all papers in SIGGRAPH recent 5 years .He serves as an associate editor for [Journal gtCVPR]and reviewer for Journal TPAMI and IJCV. His research interests fall mainly in Computer Vision, deep learning, deep reinforcement learning and robotics vision.",
            'Signature': "https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00428-1491.jpg",
            'DOB': '05 Sep 1986',
            'Email': researcher['Email'],
            'Mottos': '''{"Mottos": ["Learn the hardcore knowledge is important", "My lectures would be useless if your future career is civil servants", "Do not cheat"]}''',
            'ResearchInterest': researcher['ResearchInterest'],
            'Awards': '''{"Awards": {"Journal Reviewer": "../../static/main_style/img/uploads/awards/award-02.png", "Workshop Co-chair": "../../static/main_style/img/uploads/awards/award-01.png"}}''',
            'Co_authors': Co_authors,
            'Papers': Papers,
            'Cited_graph': Cited_graph,
            # 'Temperature': 学者在搜索种出现的次数
        })
    return data


if __name__ == '__main__':
    # features 数据
    files = get_files('./data/features')
    # print(files)
    researchers = []
    for fpath in files:
        researchers.extend(load_json(fpath))  # f: <dict>
    
    # 谷歌论文数据
    google_data = []
    google_files = get_files('./data/google_data')
    for fpath in google_files:
        google_data.extend(load_json(fpath))  # f: <dict>
        # print()
    for i in google_data:
        for j in i.values():
            print(j, end=" ")
        print()
    exit(0)
    # print(researchers)
    # print(google_data)
    # exit(0)
    # DB Data
    data = data_for_db(researchers, google_data)
    print(len(data))

    # 数据库写入
    #建立数据库连接
    db = pymysql.connect(host="127.0.0.1", user="root",password="78tZrJy8rK(0", database="scholar")
    #获取游标对象
    cursor = db.cursor()
    #创建数据库，如果数据库已经存在，注意主键不要重复，否则出错
    try:
        cursor.execute('''create table Researchers(
            ID int primary key,
            Name varchar(255),
            Avatar varchar(255),
            Title varchar(255),
            HomePage varchar(255),
            University varchar(255),
            Lab varchar(255),
            Bio varchar(255),
            Signature varchar(255),
            DOB varchar(255),
            Email varchar(255),
            Mottos varchar(255),
            ResearchInterest varchar(255),
            Awards varchar(255),
            Co_authors varchar(255),
            Papers varchar(255),
            Cited_graph varchar(255)
             )''')
    except:
        print('数据库已存在！')
    
    #插入数据语句
    query = """insert into Researchers (ID, Name, Avatar, Title, HomePage, University, Lab, Bio, 
                Signature, DOB, Email, Mottos, ResearchInterest, Awards, Co_authors, Papers, Cited_graph) values 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    #迭代读取每行数据
    #values中元素有个类型的强制转换，否则会出错的
    #应该会有其他更合适的方式，可以进一步了解
    for record in data:
        ID = record['ID']
        print("ID", type(ID), ID)
        Name = record['Name']
        Avatar = record['Avatar']
        Title = record['Title']
        HomePage = record['HomePage']
        University = record['University']
        Lab = record['Lab']
        Bio = record['Bio']
        Signature = record['Signature']
        DOB = record['DOB']
        Email = record['Email']
        Mottos = record['Mottos']
        Mottos = {
            "Mottos": [
                "Learn the hardcore knowledge is important",
                "My lectures would be useless if your future career is civil servants",
                "Do not cheat"
                ]
            }
        # ResearchInterest
        temp_dict = {}
        for idx, interest in enumerate(record['ResearchInterest']):
            temp_dict[interest] = idx * 10
            ResearchInterest = {"ResearchInterest": temp_dict}
            # Awards
            # Awards = record['Awards']
            # Co_authors = record['Co_authors']
            # Papers = record['Papers']
            # Cited_graph = {"Cited_graph": record['Cited_graph']}

        Awards = ""
        Co_authors = ""
        Papers = ""
        Cited_graph = ""

        values = (ID, str(Name), str(Avatar), str(Title), str(HomePage), str(University), str(Lab),
                    str(Bio), str(Signature), str(DOB), str(Email),
                    json.dumps(Mottos),
                    json.dumps(ResearchInterest),
                    json.dumps(Awards),
                    json.dumps(Co_authors),
                    json.dumps(Papers),
                    json.dumps(Cited_graph))
        # cursor.execute(query, values)
        try:
            cursor.execute(query, values)
        except:
            print()
            break
        else:
            print("内容写入文件成功")
    
    cursor.close()
    db.commit()
    db.close()
import pymysql
import random

file = open("./top20.txt", "r", encoding="utf8")
lines = file.readlines()
val_list = []
cnt = 0
for line in lines:
    line = line.strip('\n')
    teachers = line.split('&&')
    src = teachers[0]
    for dst in teachers[1:]:
        cnt += 1
        val_list.append((src, dst))
    # print(teachers)
file.close()
print(val_list)
random.shuffle(val_list)

db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="scholar")
cursor = db.cursor()
sql = " INSERT INTO sim (src, dst) VALUES (%s, %s) "
try:
    # 执行sql语句
    cursor.executemany(sql, val_list)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print(e)
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()


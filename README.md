# README

## TODO
1. 在 connection.html 上展示 co-author 和 cited_graph, 已完成
2. Search Bar, 已完成
3. HotSearch 页面
    3.1 需要添加收藏图标
    3.2 需要修改 es 数据
4. Search 页面, 正在做

## Structure



## Command

### RUN
python root/mobile-net-work-ee447/app_lwx.py

### 9100
/root/elasticsearch-head
grunt server

http://1.15.106.125:9100/

https://www.cnblogs.com/zhengbin/p/6144394.html

### 9200
su ela
./root/elasticsearch-6.8.14/bin/elasticsearch

### Resources
/root/mobile-net-work-ee447/static

SELECT * 
FROM Students A
WHERE name IN (SELECT TOP 3 name
                       FROM Students B
                      WHERE B.kemu = A.kemu
                      ORDER BY B.score DESC)
ORDER BY A.kemu, A.score DESC

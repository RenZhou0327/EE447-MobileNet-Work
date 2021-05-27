# README

## TODO
1. 在 connection.html 上展示 co-author 和 cited_graph, 已完成
2. Search Bar, 已完成
3. HotSearch 页面
    3.1 需要添加收藏图标, 已完成
    3.2 需要修改 es 数据
        3.2.1 lwx&zr 制定接口
        3.2.2 zr 处理 ES, lwx 用 toydata 跑通 index, search 页面的老师卡片

es:
- Researcher.Name
- Researcher.Title
- Researcher.University
- Researcher.Avatar
- Researcher.ResearchInterest

db:
- `ID`
- `Name`
- `Avatar`
- `Title`
- `HomePage`
- `University`
- `Lab`
- `Bio`: 个人简介
- `Signature`
- `DOB`: Date of Birth
- `Address`
- `Email`
- `Mottos`: "Learn the hard core knowledge" etc.
- `ResearchInterest`
- `Awards`: 获得的奖项
- `Co_authors`: 合作者
- `Papers`: 论文基本信息
- `Cited_graph`: 论文被引数量
- `Temperature`: 学者在搜索种出现的次数

4. Search 页面, 正在做

## Structure
```bash
build_data:
    buildDB.py: 建立数据库
```


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


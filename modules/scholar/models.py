from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def check_pwd(self, pwd):
        return pwd == self.password


# class SearchItem(db.Model):
#     __tablename__ = "hello"

class Researcher(db.Model):
    __tablename__ = 'Researchers'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True)
    Avatar = db.Column(db.String(100), unique=True)
    Title = db.Column(db.String(100), unique=True)
    HomePage = db.Column(db.String(100), unique=True)
    University = db.Column(db.String(100), unique=True)
    Lab = db.Column(db.String(100), unique=True)
    Bio = db.Column(db.String(100), unique=True)  # 自我介绍
    Signature = db.Column(db.String(100), unique=True)  # 签名
    DOB = db.Column(db.String(100), unique=True)  # Date of Birth
    Email = db.Column(db.String(100), unique=True)
    Mottos = db.Column(db.String(100), unique=True)
    ResearchInterest = db.Column(db.String(100), unique=True)
    Awards = db.Column(db.String(100), unique=True)
    Co_authors = db.Column(db.String(100), unique=True)  # 论文合作者
    Papers = db.Column(db.String(100), unique=True)  # 论文
    Cited_graph = db.Column(db.String(100), unique=True)  # 每年引用数量

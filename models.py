from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin
db = SQLAlchemy() #实例化数据库对象

class Bookinfo(db.Model):#图书信息表
    __tablename__ = 'bookinfo'

    isbn = db.Column(db.String(13), unique=True, primary_key = True )
    title = db.Column(db.String(200), nullable=False)
    author= db.Column(db.Text, nullable=False)
    img =db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False) 
    trade_price =db.Column(db.Integer, nullable=False) 
    retail_price =db.Column(db.Integer, nullable=False)  
    pub_date= db.Column(db.Date, nullable=False) 
    description =db.Column(db.Text, nullable=False) 

class User(UserMixin, db.Model):#用户表
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False) 
    is_admin = db.Column(db.Boolean, nullable=False ) 


class Cart(db.Model):#购物车表
    __tablename__ = 'cart'

    id = db.Column(db.Integer, unique=True, primary_key=True ) 
    uid = db.Column(db.Integer,  db.ForeignKey('user.id'))
    book_id = db.Column(db.String(13), db.ForeignKey('bookinfo.isbn') ) 
    quantity = db.Column(db.Integer, nullable=False ) 
    book = db.relationship('Bookinfo', backref='cart')   

    



# -*- coding:utf-8 -*-
"""
个性化商城首页
"""
from flask import Flask, render_template, session, redirect, url_for, request
from flask_login import  LoginManager, login_required, login_user, current_user, logout_user
from models import *
import pymysql
pymysql.install_as_MySQLdb() 
import cart, stock
import os

ROOTDIR = os.path.abspath(os.path.dirname(__file__))

APP = Flask(__name__)
APP.register_blueprint(cart.shopping_cart, url_prefix="/cart")#定义购物车蓝图
APP.register_blueprint(stock.stock, url_prefix="/stock")#库存蓝图
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://debian-sys-maint:M8nVF2jdyGLu0Tx3@localhost:3306/bookmall?charset=utf8'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = '@bookstore2021'

db.init_app(APP) #init database 
login_manager = LoginManager(APP) 
login_manager.login_view = 'login'

@login_manager.user_loader  
def load_user(user_id):
    return User.query.get(int(user_id)) 

@APP.route("/login")
def login():
    return render_template("login.html")


@APP.route("/logout")#用户注销
def logout():
    logout_user()
    return redirect("/login")


@APP.route("/do_login", methods=["POST"])#用户登录
def do_login():
    user_name = request.form.get('user_name')#获取表单提交的用户名
    password =  request.form.get('password')#密码
    # 拿着获取到的用户名和密码进行登录
    user = User.query.filter_by( username = user_name,password=password ).first() #查找该用户是否存在
    if user:
        login_user(user) 
        if user.is_admin == True:#判断是否为管理员，跳转不同地址
            return redirect('/stock')
        else:
            return redirect('/home')
    else:
        return render_template("login.html",err="Incorrect password!")#错误提示
    return redirect("/")


@APP.route("/")
@APP.route("/home")
@login_required 
def index():
    costs = 0
    num = 0 
    books = Bookinfo.query.filter(Bookinfo.stock > 0 )#查找库存大于0的书
    cart = Cart.query.filter_by(uid=current_user.id).count() #判断购物车是否为空
    if cart > 0:
        for i in Cart.query.filter_by(uid=current_user.id ).all():#遍历购物车
            num+=i.quantity #总数目
            costs += i.book.retail_price*i.quantity #计算总价
    return render_template("index.html", my_books=books,num=num,costs=costs )


@APP.route("/detail/<isbn>")
@login_required
def detail(isbn):#图书详情
    book = Bookinfo.query.get( isbn )#根据ISBN查找
    return render_template("detail.html", book=book )  


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000, debug=False)

# -*- coding:utf-8 -*-
"""
库存模块
"""
from flask import Blueprint, render_template, abort, session, redirect, request
from flask_login import login_required
from models import Bookinfo,db  
from datetime import date
stock = Blueprint("stock", __name__, static_folder="static", template_folder="templates")


@stock.route("/")
@login_required
def index():
    res = Bookinfo.query.all() #显示所有库存
    return render_template("stock.html", res = res )


@stock.route("/add_book")
@login_required
def add_book(): #显示库存页面
    return render_template("add_book.html")


@stock.route("/add_stock",methods=["POST"])
@login_required
def add_stock():  #添加图书信息
    title = request.form.get('title')
    isbn = request.form.get('isbn')
    author = request.form.get('author')
    retail = request.form.get('retail')
    trade = request.form.get('trade')
    description = request.form.get('description')
    quantity = request.form.get('quantity')
    y,m,d = request.form.get('date').split("-")#获取年月日
    pubdate = date(int(y),int(m),int(d))  
    img = request.files.get('img')
    img.save('./static/img/'+img.filename)#图片保存 
    book = Bookinfo(title=title, isbn=isbn, author=author, img= "/static/img/"+img.filename,\
         trade_price=int(trade), pub_date=pubdate, retail_price=int(retail), description=description,stock=int(quantity) )
    db.session.add(book)
    db.session.commit() 
    return render_template("add_book.html",info="Add Success!")
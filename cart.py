# -*- coding:utf-8 -*-
"""
购物车模块
"""
from flask import Blueprint, render_template, abort, session, redirect, request
from jinja2 import TemplateNotFound
from flask_login import login_required,current_user
from models import Cart,db 
shopping_cart = Blueprint("cart", __name__, static_folder="static", template_folder="templates")


@shopping_cart.route("/index")
@login_required
def index():
    total = 0
    books = Cart.query.filter_by(uid=current_user.id).all() #根据用户id查找购物车数据
    for b  in books:
        total = total + b.quantity * b.book.retail_price #遍历购物车计算总价
    return render_template("cart.html", books=books ,total=total )


@shopping_cart.route("/add/<isbn>")  
@login_required
def add_2_cart(isbn):
    """
    将物品编号是id的物品放入到用户购物车
    :param id:
    :return:
    """
    try:
        cart_item = Cart.query.filter_by(uid=current_user.id , book_id=isbn).first() 
        if cart_item is not None: #先判断该书是否已经加入购物车
            cart_item.quantity += 1 #数量加1
        else:
            item = Cart(uid = current_user.id , book_id = isbn, quantity = 1)#不在购物车就新建一条记录
            db.session.add(item)
        db.session.commit()
        return redirect('/cart/index')    
    except TemplateNotFound:
        abort(404)


@shopping_cart.route("/<isbn>/remove")
@login_required
def remove_from_cart(isbn):
    try:
        Cart.query.filter_by(uid=current_user.id,book_id=isbn).delete() #根据isbn移除购物车的书
        db.session.commit() #提交保存
        return redirect("/cart/index")
    except Exception as exception:
        abort(500)

@shopping_cart.route("/remove_all")
def remove_all():
    try:
        Cart.query.filter_by(uid=current_user.id).delete() #删除该用户所有购物车数据
        db.session.commit()#提交保存
        return redirect("/cart/index")
    except Exception as exception:
        abort(500)

@shopping_cart.route("/pay_check")
@login_required
def pay_check():
    try:
        
        res = []
        total_money = 0  #图书总价 
        tota_postage = 3 #邮费
        not_enough = []  #库存不足的书
        for item in Cart.query.filter_by(uid=current_user.id).all() : 
            if item.quantity <= item.book.stock:#判断库存是否充足
                tota_postage = tota_postage + item.quantity #邮费累加
                total_money += item.quantity * item.book.retail_price  #图书总价累加
                res.append(item)
            else:
                not_enough.append(item) #库存不足的书
        if tota_postage > 4:#根据规则邮费调整
            tota_postage = tota_postage - 2  
        else:
            tota_postage = 3
        return  render_template("check.html",tota_postage=tota_postage,total_money=total_money,res=res,not_enough=not_enough)
    except Exception as exception:
        print(exception)
        abort(500)


@shopping_cart.route("/pay_now")
@login_required
def pay_now():
    for item in Cart.query.filter_by(uid=current_user.id).all() : #遍历购物车
        if item.quantity <= item.book.stock:#库存充足则扣减对应库存
            item.book.stock-=item.quantity
    Cart.query.filter_by(uid=current_user.id).delete() #删除所有购物车数据，这里把库存不足的也删了
    db.session.commit() 
    return render_template('payment.html')

from flask import render_template
from app import app
from models.order_db import *


@app.route('/')
def index():
    return render_template('index.html',title = "Saul's Game Shop",orders = orders)

@app.route('/order/<order_id>')
def order(order_id):
    order_in = return_order_by_id(orders,order_id)
    print(order_in)
    return render_template('order.html',title = "Your Order",order = order_in)


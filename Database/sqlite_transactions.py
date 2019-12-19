from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session



engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

'''
For the following task:
1. Set the shipping date in the date_shipped column in orders table.
2. Subtract the quantity of ordered items from the items table. 

We define dispatch_order() method which accepts order_id as an argument, 
and performs the above-mentioned tasks in a transaction.
'''

from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from datetime import datetime


def dispatch_order(order_id):
    # check whether order_id is valid or not
    order = session.query(Order).get(order_id)

    if not order:
        raise ValueError("Invalid order id: {}.".format(order_id))

    if order.date_shipped:
        print("Order already shipped.")
        return

    try:
        for i in order.order_lines:
            i.item.quantity = i.item.quantity - i.quantity

        order.date_shipped = datetime.now()
        session.commit()
        print("Transaction completed.")

    except IntegrityError as e:
        print(e)
        print("Rolling back ...")
        session.rollback()
        print("Transaction failed.")

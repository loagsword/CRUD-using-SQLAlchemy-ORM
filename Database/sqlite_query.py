from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# all() method
session.query(Customer).all()

# count() method
session.query(Customer).count() # get the total number of records in the customers table
session.query(Item).count()  # get the total number of records in the items table
session.query(Order).count()  # get the total number of records in the orders table

# first() method
ession.query(Customer).first()
session.query(Item).first()
session.query(Order).first()

# get()
session.query(Customer).get(1)
session.query(Item).get(1)
session.query(Order).get(100)


# filter()
session.query(Customer).filter(Customer.first_name == 'John').all()
session.query(Customer).filter(Customer.id <= 5, Customer.town == "Norfolk").all()

# find all customers who either live in Peterbrugh or Norfolk
 
session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh', 
    Customer.town == 'Norfolk'
)).all()
 
 
# find all customers whose first name is John and live in Norfolk
 
session.query(Customer).filter(and_(
    Customer.first_name == 'John', 
    Customer.town == 'Norfolk'
)).all()
 
 
# find all johns who don't live in Peterbrugh
 
session.query(Customer).filter(and_(
    Customer.first_name == 'John', 
    not_(
        Customer.town == 'Peterbrugh', 
    )
)).all()


# IS NULL
session.query(Order).filter(Order.date_shipped == None).all()

# IS NOT NULL
session.query(Order).filter(Order.date_shipped != None).all()

# iN
session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()

# NOT IN
session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()

# BETWEEN
session.query(Item).filter(Item.cost_price.between(10, 50)).all()

# NOT BETWEEN
session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()

# LIKE
session.query(Item).filter(Item.name.like("%r")).all()

# NOT LIKE
session.query(Item).filter(not_(Item.name.like("W%"))).all()

# limit() & offset()
'''
The limit() method adds LIMIT clause to the query. 
It accepts the number of rows you want to return from the query.

The offset() method adds the OFFSET clause to the query. 
It accepts offset as an argument. 
It is commonly used with the limit() clause.
'''
# limie()
session.query(Customer).limit(2).all()
session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all()

# Offset
session.query(Customer).limit(2).offset(2).all()

# order_by() 
session.query(Item).filter(Item.name.ilike("wa%")).all()
session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all()

# join()
session.query(Customer).join(Order).all()

# use join to ger data from multiple tables:
session.query(Customer.id, Customer.username, Order.id).join(Order).all()

# Ex 2
session.query(
    Customer.first_name, 
    Item.name, 
    Item.selling_price, 
    OrderLine.quantity
).join(Order).join(OrderLine).join(Item).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
    Order.id == 1,
).all()


# outerjoin()
# It creates LEFT OUTERJOIN
session.query(        
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()


# group_by()
from sqlalchemy import func
 
session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',    
).group_by(Customer.id).scalar()


# having()
# finds the number of customers lives in each town
 
session.query(
    func.count("*").label('town_count'),    
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()










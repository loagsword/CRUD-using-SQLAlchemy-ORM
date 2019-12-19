from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# To deal with the duplicate rows in the result set 
#  the DISTINCT option can be used.
from sqlalchemy import distinct
 
session.query(Customer.town).filter(Customer.id  < 10).all()
session.query(Customer.town).filter(Customer.id  < 10).distinct().all()
 
session.query(        
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()
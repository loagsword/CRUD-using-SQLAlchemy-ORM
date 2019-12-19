from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Using raw queries
from sqlalchemy import text

session.query(Customer).filter(text("first_name = 'John'")).all()

session.query(Customer).filter(text("town like 'Nor%'")).all()

session.query(Customer).filter(text("town like 'Nor%'")).order_by(text("first_name, id desc")).all()


from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# The cast() funtion from the sqlalchemy package 
# is used for the common Casting (or converting) data operation
from sqlalchemy import cast, Date, distinct, union
 
session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all()
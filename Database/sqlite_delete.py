from sqlite_declarative import Base, Customer, Item, Order, OrderLine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


i = session.query(Item).filter(Item.name == 'Monitor').one()
i

session.delete(i)

# This commit removes the Monitor from the items table.
session.commit()

# To delete multiple records at once use the delete() method
# of the Query object.

session.query(Item).filter(
    Item.name.ilike("W%")
).delete(synchronize_session='fetch')
session.commit()
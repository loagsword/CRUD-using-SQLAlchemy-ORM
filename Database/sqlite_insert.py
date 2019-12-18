from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlite_declarative import Base, Customer, Item, Order, OrderLine


# Create Engine that stores data in web/Sqlite-Data/example.db file
# engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
engine = create_engine('sqlite:///Sqlite-Data/example.db')
Base.metadata.bind = engine


# Connect to sqlite server using absolute path
# https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/
DBSession = sessionmaker(bind=engine)

session = DBSession()

# Inserting Data
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
)


session.add_all([c1, c2])
session.commit()
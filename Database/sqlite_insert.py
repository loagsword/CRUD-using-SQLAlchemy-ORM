from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


# Create Engine that stores data in web/Sqlite-Data/example.db file
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

# Connect to sqlite server using absolute path
# https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/
Session = sessionmaker(bind=engine)

session = Session()

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
c1, c2

c1.first_name, c1.last_name
c2.first_name, c2.last_name

session.add(c1)
session.add(c2)

c1.id, c2.id
session.add_all([c1, c2])
session.new
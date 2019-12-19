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

c3 = Customer(
            first_name = "John", 
            last_name = "Lara", 
            username = "johnlara", 
            email = "johnlara@mail.com", 
            address = "3073 Derek Drive",
            town = "Norfolk"
)
 
c4 = Customer(          
            first_name = "Sarah", 
            last_name = "Tomlin", 
            username = "sarahtomlin", 
            email = "sarahtomlin@mail.com",
            address = "3572 Poplar Avenue",
            town = "Norfolk"        
)
 
c5 = Customer(first_name = 'Toby', 
              last_name = 'Miller', 
              username = 'tmiller', 
              email = 'tmiller@example.com', 
              address = '1662 Kinney Street',
              town = 'Wolfden'
             )
 
c6 = Customer(first_name = 'Scott', 
              last_name = 'Harvey', 
              username = 'scottharvey', 
              email = 'scottharvey@example.com', 
              address = '424 Patterson Street',
              town = 'Beckinsdale'
             )



session.add_all([c1, c2, c3, c4, c5, c6])
session.commit()


i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)
 
session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()


o1 = Order(customers = c1)
o2 = Order(customers = c1)
 
line_item1 = OrderLine(order = o1, item = i1, quantity =  3)
line_item2 = OrderLine(order = o1, item = i2, quantity =  2)
line_item3 = OrderLine(order = o2, item = i1, quantity =  1)
line_item3 = OrderLine(order = o2, item = i2, quantity =  4)
 
session.add_all([o1, o2])
 
session.commit()
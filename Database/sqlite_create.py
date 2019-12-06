from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
session = Session(bind=engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://user:password@localhost/db_name') # leaving this like this for now, if you want to run it on local you should create your own postgres db with the tables following the same structure as in the /models folder

Session = sessionmaker(bind=engine)

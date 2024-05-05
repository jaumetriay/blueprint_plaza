from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = 'property'

    premise_id = Column(Integer, primary_key=True)
    base_value = Column(Float)
    expected_value = Column(Float)
    description = Column(String)

# # To create the table in the database, you can use the `create_all` method of the base class
# engine = create_engine('postgresql://username:password@localhost/dbname')
# Base.metadata.create_all(engine)
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

class License(Base):
    """
    License object
    """
    __tablename__ = 'licenses'

    id = Column(Integer, primary_key=True)
    """ Primary key """
    name = Column(String(255))
    
    age_group = Column(String(255))
    
    household_type = Column(String(255))
    
    apartment_type = Column(String(255))
    
    life_situation = Column(String(255))
    
    paid = Column(Integer)
  
    def __repr__(self):
        """ String representation of the object """
        return "<License (name='%s')>" % (self.name)

DATABASE_URL = os.environ['DATABASE_URL']
""" Database URI string """
db = create_engine(DATABASE_URL)
""" Database connection """
Session = sessionmaker(bind=db)
""" Database session """
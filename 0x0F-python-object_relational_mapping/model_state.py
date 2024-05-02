#!/usr/bin/python3
"""  contains the class definition of a State and an instance 
Base = declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
metadata = MetaData()
Base = declarative_base(metadata)

class State(Base):
    """ state class """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

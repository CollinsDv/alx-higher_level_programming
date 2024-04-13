#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base():
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# declarative base class
Base = declarative_base()

# link to table
class State(Base):
    """define a class state"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

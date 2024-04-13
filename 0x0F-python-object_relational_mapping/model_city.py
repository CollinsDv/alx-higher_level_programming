#!/usr/bin/python3
"""base class definition for city"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(autoincrement = True, Integer, unique = True,
            nullable = False, primary_key = True)
    name = Column(String(128), nullable = False)
    state_id = Column(Integer, nullable = False, ForeignKey('states.id'))

#!/usr/bin/python3
"""base class definition for city"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """defining cities class to be mapped to table"""
    __tablename__ = 'cities'

    id = Column(autoincrement = True, Integer,
            nullable = False, primary_key = True)
    name = Column(String(128), nullable = False)
    state_id = Column(Integer, nullable = False, ForeignKey('states.id'))

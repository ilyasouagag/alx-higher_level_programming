#!/usr/bin/python3
"""ython file that contains the class definition of a State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class State(Base):
    """conatains id and name of each state"""
    __tablename__ = "states"
    id = Column(Integer,unique=True,nullable=False,primary_key=True)
    name = Column(String(128),nullable=False)

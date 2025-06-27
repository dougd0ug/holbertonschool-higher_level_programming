#!/usr/bin/python3
"""
Define Class State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Defin class State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    name = Column(String(128), nullable=False)

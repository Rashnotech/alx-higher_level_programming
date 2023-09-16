#!/usr/bin/python3
""" a module that contains class definition of City """

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class City(Base):
    """ a City class that inherit from Base class"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

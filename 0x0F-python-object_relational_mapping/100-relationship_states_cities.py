#!/usr/bin/python3
""" a script that creates state with city from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbase), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    city = City(name='San Francisco', state=State(name='California'))
    session.add(city)
    session.commit()

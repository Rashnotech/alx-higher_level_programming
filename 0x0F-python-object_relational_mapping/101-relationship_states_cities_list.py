#!/usr/bin/python3
""" a script that lists all state objects corresponding city object"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    count = 1
    city_state = session.query(State).order_by(State.id).all()
    for state in city_state:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('{}{}: {}'.format(' ' * 4, city.id, city.name))

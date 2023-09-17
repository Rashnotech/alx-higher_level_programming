#!/usr/bin/python3
""" a script that lists all city objects from database """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from relationship_state import State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

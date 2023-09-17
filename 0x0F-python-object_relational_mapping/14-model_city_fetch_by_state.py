#!/usr/bin/python3
""" a model that print all city object from database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities_states = session.query(City,
                                  State).filter(City.state_id
                                                == State.id).order_by(City.id)
    for city, state in cities_states:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

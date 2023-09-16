#!/usr/bin/python3
""" a script that deletes the name of a state object that start with has a"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    if states:
        for state in states:
            session.delete(state)
        session.commit()
    else:
        pass

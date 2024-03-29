#!/usr/bin/python3
"""
Script that prints the first state object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """
    Setting the session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Fecthing data
    """
    Louisiana = State()
    Louisiana.name = 'Louisiana'

    session.add(Louisiana)
    session.commit()

    new_instance = session.query(State).filter(
        State.name == Louisiana.name).order_by(State.id).first()
    if new_instance:
        print(new_instance.id)
    else:
        print('error')

    session.close()

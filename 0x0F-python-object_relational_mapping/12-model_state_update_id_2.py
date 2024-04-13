#!/usr/bin/python3
"""generate query to database that adds an object to it
"""

from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    # initialize a session to communicate with database
    session = Session()

    # obtain object
    obj_to_update = session.query(State).filter(State.id == 2).first()
    # update
    obj_to_update.name = 'New Mexico'
    # save
    session.commit()

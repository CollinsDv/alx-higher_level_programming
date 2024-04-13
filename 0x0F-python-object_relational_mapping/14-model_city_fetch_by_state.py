#!/usr/bin/python3
"""prints contents of a database joined to another
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print('{0}: ({1}) {2}'.format(state.name, city.id, city.name))

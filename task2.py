from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///task2.db')
Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    passport_id = Column("passport_id", Integer)
    flight_id = Column(Integer, ForeignKey("Flight.id"))

    def __init__(self, first_name, last_name, passport_id):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_id = passport_id

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.passport_id}"


class Flight(Base):
    __tablename__ = 'Flight'
    id = Column(Integer, primary_key=True)
    destination = Column("destination", String)
    airplane_id = Column("airplane_id", Integer)
    max_num_people = Column("max_num_people", Integer)
    num_people = Column("num_people", Integer)
    flight_id = relationship("User")

    def __init__(self, destination, airplane_id, max_num_people, num_people=0):
        self.destination = destination
        self.airplane_id = airplane_id
        self.max_num_people = max_num_people
        self.num_people = num_people

    def __repr__(self):
        return f"{self.id} {self.destination} {self.airplane_id} {self.max_num_people} {self.num_people}"


Base.metadata.create_all(engine)

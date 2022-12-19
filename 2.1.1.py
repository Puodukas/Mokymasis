from task2 import User, Flight
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///task2.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - pridėti naują informacija apie skrydi \n2 - pridėti savo vardą, pavardę\n "))

    if pasirinkimas == 1:
        destination = input("Iveskite keliones vieta ")
        airplane_id = int(input("iveskite lektuvo id "))
        max_num_people = int(input("Iveskite kiek max zmoniu telpa "))
        flight = Flight(destination, airplane_id, max_num_people)
        session.add(flight)
        session.commit()

    if pasirinkimas == 2:
        vardas = input("Iveskite varda ")
        pavarede = input("Iveskite pavarde ")
        passport = input("Iveskite paso id ")
        user = User(vardas, pavarede, passport)
        session.add(user)
        session.commit()

    if pasirinkimas ==4:
        zmogai = session.query(User, Flight).all()
        if max_num_people == num_people:
            print("skrydis pilnai užimtas ir jo rinktis jau negalima")
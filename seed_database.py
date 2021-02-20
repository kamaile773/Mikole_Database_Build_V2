"""Script to seed database."""
"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
from model import *

import crud
import server

os.system('dropdb mikole')
os.system('createdb mikole')

connect_to_db(server.app)
db.create_all()

# Load movie data from JSON file
with open('data/partypackages.json') as f:
    partypackages_data = json.loads(f.read())

# Create PartyPackages, store them in list

partypackages_in_db = []
for package in partypackages_data:
    package_to_save = Party_Package(title=package['title'],
                                    overview=package['overview'],
                                    party_includes=package['party_includes'],
                                    qtyguest=package['qtyguest'],
                                    cost=package['cost'])
    db.session.add(package_to_save)

# Create Testing Staff members

kjoe_staff = Staffer(fname = "Kamaile",
                     lname = "Carrell-Joe", 
                     dept = "Host", 
                     phone_num = "8085101168",
                     email = "email@kjoe.com",
                     pay_grade = "50.00",
                     work_status = "Exempt",
                     emp_exceptions = "GL, MAX, T:H,K,SUTD", 
                     availability = "SWTFS",
                     location = "SF BAY")

ajoe_staff = Staffer(fname = "Adam",
                     lname = "Joe", 
                     dept = "Kitchen", 
                     phone_num = "1234567890",
                     email = "email@email.com",
                     pay_grade = "30.00",
                     work_status = "Hourly",
                     emp_exceptions = "NL, MAXSilver, T:K,ST", 
                     availability = "SFS",
                     location = "SF BAY"
                     )

anj_staff = Staffer(fname = "AddiDJ",
                     lname = "Joe", 
                     dept = "Entertainment", 
                     phone_num = "8081234567",
                     email = "email43@email.com",
                     pay_grade = "350.00",
                     work_status = "Exempt",
                     emp_exceptions = "GL, MAXGOLD2PLAT", 
                     availability = "TFS",
                     location = "SF BAY"
                     )

rjoe_staff = Staffer(fname = "Reasunshine",
                     lname = "Joe", 
                     dept = "MANG", 
                     phone_num = "5557655432",
                     email = "email2@email.com",
                     pay_grade = "6000.00",
                     work_status = "ExemptMAN",
                     emp_exceptions = "All", 
                     availability = "SMTS",
                     location = "SF BAY"
                     )

knjoe_staff = Staffer(fname = "Koa",
                     lname = "Joe", 
                     dept = "SU/TD", 
                     phone_num = "5557655432",
                     email = "email5@email.com",
                     pay_grade = "25.00",
                     work_status = "Hourly",
                     emp_exceptions = "T:H,K,SUTD", 
                     availability = "STFS",
                     location = "SF BAY"
                     )

# Create Testing Client members

client0 = Client(name= "June Bug", email= "howdy@yahoo.com", client_phone_num="8088081122")

# Create Test Event

lots_party = Event(goh_name = "Kat Huber-Juma", added_details= "Just Because Shes Awesome", event_location = "SF BAY", client= client0, partypackage= package_to_save)

# Create Test PartyStaffer

lots_party_staffers = ParrtyStaffer(event=lots_party, staffer=kjoe_staff)


db.session.add(kjoe_staff)
db.session.add(ajoe_staff)
db.session.add(anj_staff)
db.session.add(rjoe_staff)
db.session.add(knjoe_staff)
db.session.add(client0)
db.session.add(lots_party)

db.session.commit()
    
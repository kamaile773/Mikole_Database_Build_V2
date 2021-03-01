"""CRUD Operations."""

from model import db, Party_Package, Staffer, Client, Event, connect_to_db

#from model import db, Client, Event, Party_Package, Inventory, Staffer, PartyStaffer, connect_to_db


"""Party Packages Section: Class is Party_Package, tablename=partypackages"""

def create_partypackages(title, overview, party_includes, qty_of_guest, cost):
    """Create and return a new party package."""

    partypackage = Party_Package(title=title, overview=overview, party_includes=party_includes, qtyguest=qtyguest, cost=cost)

    db.session.add(partypackage)
    db.session.commit()

    return partypackage

def get_partypackages():
    """Return all partypackages."""

    return Party_Package.query.all()

def get_partypackages_id(purchase_id):
    """Return Party Package by PK."""
    
    return Party_Package.query.get(purchase_id)

"""Staff Section: Class Staffer, tablename=staffers"""

def get_partypackage(title):

    package = Party_Package.query.filter_by(title=title).first()

    return package.purchase_id

def get_staff_by_phone_num(phone_num):
    """Return Staff by their phone number."""

    return Staffer.query.filter_by(phone_num=phone_num).first()

"""Client Section: Client tablename=clients"""

def add_client(name, client_phone_num, email):
    """Registration"""
    new_client = Client(name=name, client_phone_num=client_phone_num, email=email)

    db.session.add(new_client)
    db.session.commit()

    return new_client

def get_clients():
    """Return all users."""

    return Client.query.all()

def get_client_record(client_id):

    return Client.query.get(client_id)

def get_client_by_phone_num(phone_num):
    """Return client by their phone number."""

    return Client.query.filter_by(phone_num=phone_num).first()

def get_client_id(email):

    client = Client.query.filter_by(email=email).first()
    
    return client.client_id

def get_event_by_id(event_id):
    """Get Event By Id"""

    return Event.query.get(event_id)

def add_event(goh_name, purchase_id, date_of_event, event_location, client_id, added_details):
    """Add Event"""

    add_event = Event(goh_name=goh_name, purchase_id=purchase_id, date_of_event=date_of_event, event_location=event_location, client_id=client_id, added_details=added_details)

    db.session.add(add_event)
    db.session.commit()

    return add_event

def get_events():
    """Return all events."""

    return Event.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
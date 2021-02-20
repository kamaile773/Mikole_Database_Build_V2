"""CRUD Operations."""

from model import db, Party_Package, connect_to_db

#from model import db, Client, Event, Party_Package, Inventory, Staffer, PartyStaffer, connect_to_db


"""Party Packages Section: Class is Party_Package, tablename=partypackages"""
"""Get All Party Packages"""

def create_partypackages(title, overview, party_includes, qty_of_guest, cost):
    """Create and return a new party package."""

    partypackage = Party_Package(title=title, overview=overview, party_includes=party_includes, qtyguest=qtyguest, cost=cost)

    db.session.add(partypackage)
    db.session.commit()

    return partypackage

def get_partypackages():
    """Return all partypackages."""

    return Party_Package.query.all()

def get_partypackages_by_id(purchase_id):
    """Return Party Package by PK."""

    return Party_Package.query.get(purchase_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

"""Create Registration and Client id """
# def register_client():

#     clientregistration = client(clientname = cfullname, email = cemail, clientphone = cphone_num, checkin = client_checkin)

#     db.session.add(clientregistration)
#     db.session.commit()

#     return clientregistration

# def get_clients():
#     """Return all users."""

#     return Client.query.all()
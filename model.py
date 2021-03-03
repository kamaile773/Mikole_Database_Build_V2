"""Models for Mikole app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Party_Package(db.Model):
    """Party packages."""

    __tablename__ = 'partypackages'

    purchase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    party_includes = db.Column(db.Text)
    cost = db.Column(db.Float)
    qtyguest = db.Column(db.Integer)

    def __repr__(self):
        return f'<Party_Package purchase_id={self.purchase_id} title={self.title}>'

class Staffer(db.Model):
    """Staff Members."""

    __tablename__ = 'staffers'

    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    dept = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    pay_grade = db.Column(db.Float)
    work_status = db.Column(db.String)
    emp_attributes = db.Column(db.String)
    emp_exceptions = db.Column(db.String)
    availability = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return f'<Staffer staff_id={self.staff_id} dept={self.dept} fname={self.fname} lname={self.lname} location={self.location}>'


class PartyStaffer(db.Model):
    """Party Staff Members."""

    __tablename__ = 'partystaffers'

    partystaff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    staffer_id = db.Column(db.Integer, db.ForeignKey('staffers.staff_id'))

    event = db.relationship('Event', backref='partystaffers')
    staffer = db.relationship('Staffer', backref='partystaffers')

    def __repr__(self):
        return f'<PartyStaffer partystaff_id={self.partystaff_id}>'


class Client(db.Model):
    """A user. Class will include Clients Info and Event Needs."""

    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    client_phone_num = db.Column(db.String(120))
    checkin = db.Column(db.String(120))  

    def __repr__(self):
        return f'<Client client_id={self.client_id} name={self.name} email={self.email}>'


class Event(db.Model):
    """Unique Event selection set by Client."""

    __tablename__ = 'events'
    
    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goh_name = db.Column(db.String(50))
    date_of_event = db.Column(db.DateTime)
    added_details = db.Column(db.String)
    event_location = db.Column(db.String)
    qtyguest = db.Column(db.Integer)
    purchase_id = db.Column(db.Integer, db.ForeignKey('partypackages.purchase_id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    
    client = db.relationship('Client', backref='events')
    partypackage = db.relationship('Party_Package', backref='events')
    
    def __repr__(self):
        return f'<Event event_id={self.event_id} client={self.client} goh_name={self.goh_name} qtyguest={self.qtyguest} partypackage={self.partypackage} date_of_event={self.date_of_event} event_location{self.event_location}>'

def connect_to_db(flask_app, db_uri='postgresql:///mikole', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app

    connect_to_db(app)



"""Define client Email to send from event selection."""
# def client_send_email(a,b,c,d,e,f):
#     # creates SMTP session 
#     s = smtplib.SMTP('smtp.gmail.com',821) 
#     # start TLS for security 
#     s.starttls() 
#     # Authentication 
#     s.login("sample_mikola@gmail.com", "testing@123") 
    
#     #t = time.localtime()
#     #current_time = time.strftime("%H:%M:%S", t)   
#     # message to be sent 
#     text = "Thank you Client for visiting us,\n Client Name:\t"+ a +"\n Client Phone:\t"+ c +"\n Check-in Time:\t"+ d+"IST"+"\n Check-out Time:\t"+ e +"\n Party Staffer Name:\t" 
#     subject = "Thank you Visiting us"
#     message = 'Subject: {}\n\n{}'.format(subject, text)
#     # sending the mail 
#     s.sendmail("sample_mikola@gmail.com", b, message) 
        
#     # terminating the session 
#     s.quit()   




# """Define Party Staffer Email to send from event selection."""

# # def partystaffer_send_email(m,n,o,p,q):
# #     # creates SMTP session 
# #     s = smtplib.SMTP('smtp.gmail.com',587) 
# #     # start TLS for security 
# #     s.starttls() 
# #     # Authentication 
# #     s.login("sample_mikola@gmail.com", "testing@123") 
    

# #     # message to be sent 
# #     text = "Hi Staff,\n Client Name:\t"+ m +"\n Client Email:\t"+ n +"\n Client Phone\t"+ o+"\n Checkin Time:\t"+ p+"IST"+"\n client had just check in"
# #     subject = "Client has just checked in"
# #     message = 'Subject: {}\n\n{}'.format(subject, text)
# #     # sending the mail 
# #     s.sendmail("sample_mikola@gmail.com", q, message) 
        
# #     # terminating the session 
# #     s.quit()     


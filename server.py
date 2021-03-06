"""Mikole party service application Flask server"""

from flask import Flask, render_template, redirect, flash, session, request, url_for
from flask_session import Session
import jinja2
import send_sms
# from flaskext.mail import Message
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = 'nihq8ruwetu&(*^iaifj'



@app.route("/")
def homepage():
    """Return homepage."""

    party_packages_list = crud.get_partypackages()

    return render_template("homepage.html", party_packages_list=party_packages_list)

"""Party Packages"""

@app.route('/partypackages')
def list_party_packages():
    """List all Party Packages."""

    party_packages_list = crud.get_partypackages()

    return render_template('party_packages.html', party_packages_list=party_packages_list)

#Passing string /partypackages/<purchase_id> as a agru to app.route= means 
# that when we go localhost:5000/ it directs it here
@app.route('/partypackages/<purchase_id>')
def show_packdets(purchase_id):
    """Show details on a particular party package."""

    partypackage = crud.get_partypackages_id(purchase_id)

    return render_template('partypackages_details.html', partypackage=partypackage)


#Create routes for staffers: View all, GET individuals, Create new staff, Staff login"""
@app.route('/staffers')
def all_staffers():
    """View all Staffers."""

    staffers = crud.get_staffers()

    return render_template(staffers=staffers)

@app.route('/staffer_login', methods=['POST'])
def staffer_login():
    """Create a staffer login."""

    username = request.form['username']
    phone_num = request.form['phone_num']

    staffer_login_pn = crud.get_staff_by_phone_num(phone_num)
    
    if staffer_login_pn == None:
        flash('Wrong password!')
        return redirect('/staffer_login')
    else:
        flash(f'You are logged in as {username}.')
        session['staffer'] = username

    return redirect('/scheduled_events')

#Passing this string /staffer_login as a agru to app.route= means that when we go localhost:5000/staffer_login it directs it here
@app.route('/staffer_login')
def staffers_login():
    """Create a staffer login."""

    return render_template('staffer_index.html')

@app.route('/staffer_logout')
def logout():
    logout_staffer()
    flash('You were logged out.', 'success')
    return redirect(url_for('staffer_login'))

@app.route('/staffers/<staff_id>')
def show_staffer(staff_id):
    """Show details on a particular user."""

    staffer_info = crud.get_staffer_info_by_id(staff_id)

    return render_template(staffer_info=staffer_info)


"""Clients Routes"""
@app.route('/client_registration')
def client_registration():
    """Create a client profile for event and database"""

    return render_template('client_index.html')
    
@app.route('/client_registration', methods=['POST'])
def register_client():
    """Create a new client."""

    name = request.form.get('name')
    client_phone_num = request.form.get('client_phone_num')
    email = request.form.get('email')
    print(name, client_phone_num, email)

    new_client = crud.add_client(name, client_phone_num, email)

    if new_client is not None:
        flash('Account created!')
        session['clientName'] = new_client.name
        session['clientEmail'] = new_client.email
        party_packages_list = crud.get_partypackages()
        return render_template('event_create.html', new_client=new_client, party_packages_list=party_packages_list)
    else:
        flash('No information entered please try again')
        return redirect('/')

#Client log in Feature
@app.route('/client_login', methods=['POST'])
def client_login():
    """Create a client login."""

    username = request.form['username']
    client_phone_num = request.form['client_phone_num']

    client = crud.get_client_phone_num(client_phone_num)
    
    if client == None:
        flash('Wrong password!')
        return redirect('/client_login')
    else:
        flash(f'You are logged in as {username}.')
        session['clientEmail'] = client.email
        session['client'] = client.client_id
        session['client'] = client.client_phone_num
    return redirect(url_for('client_view', client=client))
        #NEED TO ADD A QUEREY PAGE FOR PARTY 

@app.route('/client_login')
def clients_login():
    """Create a client login."""

    return render_template('client_login_index.html')

@app.route('/client_logout')
def clients_logout():
    logout_client()
    flash('You were logged out.', 'success')
    return redirect(url_for('clients_login'))

@app.route('/clients')
def all_clients():
    """View all users."""

    clients = crud.get_clients()

    return render_template(clients=clients)

@app.route('/clients/<client_id>')
def show_client(client_id):
    """Show details on a particular user."""

    client_ids = crud.get_client_record(client_id)

    return render_template(client_ids=client_ids)

@app.route ('/clientevents')
def client_view():
    """Display clients event"""

    partyInfo = crud.get_client_events(session['client_login_pn'])

    return render_template('client_events.html', partyInfo=partyInfo)


@app.route('/clientthank')
def clientthank():
    """clientthank"""

    message = send_sms.text_client.messages.create(
        to="+15103773852", 
        from_="+18082078922",
        body="Hello, Thank you for your reservation! Your Event Confirmation # is ME"
        )

    # print('\n************message.sid******************')
    # print(message.sid)
    return render_template('client_thank.html')

"""Events Routes"""

@app.route('/create_event')
def create_event_get():
    party_packages_list = crud.get_partypackages()
    #clientid = crud.get_client_id(session['clientEmail'])
    
    #session['clientName'] = new_client.name
    
    return render_template('event_create.html', party_packages_list=party_packages_list)



@app.route('/create_event', methods=['POST'])
def create_event():
    """Create an Event"""
    
    client_id = crud.get_client_id(session['clientEmail'])
    goh_name = request.form['goh_name']
    partypackage = request.form['partypackage']
    purchase_id = crud.get_partypackage(partypackage)
    date_of_event = request.form['date_of_event']
    added_details = request.form['added_details']
    qtyguest = request.form['qtyguest']
    event_location = request.form['event_location']

    event = crud.add_event(goh_name, purchase_id, date_of_event, qtyguest, event_location, client_id, added_details)


    return redirect('/clientthank')


@app.route('/events/<event_id>')
def show_event(event_id):
    """Show details on a particular event."""

    event = crud.get_event_by_id(event_id)

    return render_template('client_thank.html', event=event)

@app.route('/scheduled_events')
def show_staffers_events():

    events = crud.get_events_by_location(session['staffer'])
    
    return render_template('scheduled_events.html', events=events)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
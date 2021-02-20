"""Mikole party service application Flask server"""

from flask import Flask, render_template, redirect, flash, session
import jinja2
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = 'nihq8ruwetu&(*^iaifj'


@app.route("/")
#@app.route("/homepage", methods=["GET", "POST"])
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

@app.route('/partypackages/<purchase_id>')
def show_partypackages(purchase_id):
    """Show details on a particular party package."""

    partypackages = crud.get_partypackages_by_id(purchase_id)

    return render_template('partypackages_details.html', partypackages=partypackages)

#Create routes for staffers: View all, GET individuals, Create new staff, Staff login"""

@app.route('/staffers')
def all_staffers():
    """View all Staffers."""

    staffers = crud.get_staffers()

    return render_template(staffers=staffers)

@app.route('/staffers', methods=['GET','POST'])
def staffers_login():
    """Create a staffer login."""

    username = request.form['lname']
    sphone_num = request.form['phone_num']

    staffer_login_pn = crud.get_staff_by_phone_num(phone_num)
    # option 1 on if statement
    
    if request.method == 'POST':
        if staffer_login_pn != ['sphone_num']:
            flash('Wrong password!')
        else:
            flash(f'You are logged in as {username}.')
            return redirect('Staff/staffers_layout.html')
    return render_template('homepage.html', staffer_login_pn=staffer_login_pn)


@app.route('/staffers/<staff_id>')
def show_staffer(staff_id):
    """Show details on a particular user."""

    staffer_info = crud.get_staffer_info_by_id(staff_id)

    return render_template(staffer_info=staffer_info)



"""Clients Routes"""

# @app.route('/clients')
# def all_clients():
#     """View all users."""

#     clients = crud.get_clients()

#     return render_template('clients.html', clients=clients)


# @app.route('/clients', methods=['GET','POST'])
# def register_clients():
#     """Create a new client."""

#    if request.method == 'POST':
#     cfname = request.form.get('firstname')
#     clname = request.form.get('lastname')
#     cfullname = cfname+" " +lastname
#     cphone_num = request.form.get('phone_num')
#     cemail = request.form.get('email')
#     clientevent = time.localtime()
#     client_checkin = time.strftime("%H:%M:%S", clientevent)
    
#     client = crud.get_client_by_phone_num(phone_num)
#     if client:
#         flash('Cannot create an account with that phone number. Try again.')
#     else:
#         crud.create_client(name, phone_num)
#         flash('Account created! Please log in with your phone number.')

#     return redirect('/')

# @app.route('/clients/<client_id>')
# def show_client(client_id):
#     """Show details on a particular user."""

#     client = crud.get_client_by_id(client_id)

#     return render_template('client_details.html', client=client)

# @app.route('/clients', methods=['GET','POST'])
# def register_clients():
#     """Create a new client."""
#    if request.method == 'POST':
#     name = request.form.get('name')
#     phone_num = request.form.get('phone_num')
#     email = request.form.get('email')
    
#     client = crud.get_client_by_phone_num(phone_num)
#     if client:
#         flash('Cannot create an account with that phone number. Try again.')
#     else:
#         crud.create_client(name, phone_num)
#         flash('Account created! Please log in with your phone number.')

#     return redirect('/')

# Events Routes
# @app.route('/events')
# def create_events():
#     """Create an Event"""

#     """Tracking order cost"""
#     selected_partypackage = 0

#     """create a list of party package selection"""
#     party_package = []

#     """Get event dictionary out of session"""
#     event_cart = session.get("event", {})

#     """Loop over the event dictionary"""
#     for event_id in 


# @app.route('/events/<event_id>')
# def show_event(event_id):
#     """Show details on a particular event."""

#     event = crud.get_event_by_id(event_id)

#     return render_template('event_details.html', event=event)

# @app.route('/events')
# def all_events():
#     """View all events."""

#     events = crud.get_events()

#     return render_template('all_events.html', events=events)





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
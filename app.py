from flask import render_template, Flask, request, make_response
from models import Calendar, Event

app = Flask(__name__)


##################### HOME PAGE #########################
@app.route("/")
def home():
    data = {"name": "JI"}
    return render_template("index.html", **data)


##################### CALENDAR ROUTES #########################
"""
Routes:
    1. GET /search/calendars
    2. GET /create/calendar
    3. POST /create/calendar
    4. GET /calendar/<calendar_id>
"""
@app.route("/search/calendars")
def calendar_search():
    calendars = Calendar.all()  # .filter()
    return render_template("calendar_search.html", calendars=calendars)


@app.route("/create/calendar", methods=["GET"])
def calendar_form():
    return render_template("calendar_create.html", fields=Calendar.fields)


@app.route("/create/calendar", methods=["POST"])
def new_calendar():
    try:
        Calendar.save_from_form_data(request)
    except:
        return make_response("Missing fields!", 400)
    return "<p>Calendar created</p>"

@app.route("/calendar/<calendar-id>")
def calendar_page(calendar_id):
    calendar = Calendar.get(calendar_id)
    if not calendar:
        return make_response("<p>Calendar not found</p>", 404)
    return render_template("calendar_page.html", **calendar.to_dict())

##################### EVENT ROUTES #########################
"""
Routes:
    1. GET /search/events
    2. GET /create/event
    3. POST /create/event
    4. GET /event/<event_id>
"""
@app.route("/create/event", methods=["GET"])
def event_form():
    return render_template("event_create.html", fields=Event.fields)


@app.route("/create/event", methods=["POST"])
def new_event():
    try:
        Event.save_from_form_data(request)
    except:
        return make_response("Missing fields!", 400)
    return "<p>Event created</p>"


@app.route("/search/events")
def event_search():
    events = Event.all()  # .filter()
    return render_template("event_search.html", events=events)


@app.route("/event/<event_id>")
def event_page(event_id):
    event = Event.get(event_id)
    if not event:
        return make_response("<p>Event not found</p>", 404)
    return render_template("event_page.html", **event.to_dict())

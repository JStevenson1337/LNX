from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    data = {"name":"JI"}
    return render_template("index.html", **data)

@app.route("/search/calendar_search")
def calendar_search():
    data = {}
    return render_template("calendar_search.html", **data)

@app.route("/search/calendar_create")
def calendar_create():
    data = {}
    return render_template("calendar_create.html", **data)

@app.route("/search/event_search")
def event_search():
    data = {}
    return render_template("event_search.html", **data)


@app.route("/search/event_create")
def event_create():
    data = {}
    return render_template("event_create.html", **data)

@app.route("/search/event_page")
def event_page():
    data = {}
    return render_template("event_page.html", **data)


@app.route("/search/public_event")
def public_event():
    data = {}
    return render_template("public_event.html", **data)


@app.route("/search/public_create")
def public_create():
    data = {}
    return render_template("public_create.html", **data)

@app.route("/search/private_event")
def private_event():
    data = {}
    return render_template("private_event.html", **data)

@app.route("/search/private_create")
def private_create():
    data = {}
    return render_template("private_create.html", **data)

@app.route("/search/semi_private")
def semi_private():
    data = {}
    return render_template("semi_private.html", **data)

@app.route("/search/semi_private_create")
def semi_private_create():
    data = {}
    return render_template("semi_private_create.html", **data)

@app.route("/search/calendar_page")
def calendar_page():
    data = {}
    return render_template("calendar_page.html", **data)

@app.route("/search/public_calendar")
def public_calendar():
    data = {}
    return render_template("public_calendar.html", **data)

@app.route("/search/public_calendar_create")
def public_calendar_create():
    data = {}
    return render_template("public_calendar_create.html", **data)

@app.route("/search/private_calendar")
def private_calendar():
    data = {}
    return render_template("private_calendar.html", **data)

@app.route("/search/private_calendar_create")
def private_calendar_create():
    data = {}
    return render_template("private_calendar_create.html", **data)

"""
# What do we need....

Pages:

Home page
Calendar Search
Event Search
Event Page
Public Event
Private Event
Semi-Private
Calendar Page
Public Calendar
Private Calendar

"""

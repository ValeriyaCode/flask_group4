from flask import Flask, render_template

app = Flask(__name__)

ALL_EVENTS = [
    {"title": "morning meeting", "time": "09:30", "participants": ["Anna", "Oleh"]},
    {"title": "code review", "time": "14:00", "participants": ["Max", "Lera", "Ira"]},
    {"title": "team meeting", "time": "11:00", "participants": ["Sofia", "Danilo"]},
    {"title": "project planning", "time": "16:45", "participants": ["Ivan"]},
]


@app.route('/')
@app.route('/events')
def events():
    sort_events = sorted(ALL_EVENTS, key=lambda event: event["time"])
    return render_template('events.html', events=sort_events)

app.run(debug=True)

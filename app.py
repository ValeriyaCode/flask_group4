from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    years, days = None, None

    if request.method == 'POST':
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')

        day, month, year = int(day), int(month), int(year)

        birthday = date(year, month, day)
        today = date.today()

        years = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            years -= 1

        days = (today - birthday).days

    return render_template('index.html', years=years, days=days)

app.run(debug=True)

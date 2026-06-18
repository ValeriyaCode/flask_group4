import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/for_student')
def for_student():
    return render_template('for_student.html', name='Lera')

@app.route('/teachers')
def teachers():
    all_teachers = ['Seva', 'Georgiy', 'Vlad']
    return render_template('teachers.html', teachers=all_teachers)


@app.route('/surprise')
def surprise():
    win = random.choice([True, False])
    discount = random.randint(1000, 10000)
    return render_template('surprise.html', is_win=win, discount=discount)


app.run(debug=True)

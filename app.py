from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 12 and phone.startswith('380')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')

        if not is_valid_phone(phone):
            flash('Is not a valid phone number')
            return redirect(url_for('register'))
        else:
            flash(f'Good, {name}')
            return redirect(url_for('index'))

    return render_template('register.html')


app.run(debug=True)

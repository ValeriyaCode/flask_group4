from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import init_db
from actions_db import *
from werkzeug.security import generate_password_hash, check_password_hash

# імпортація blueprint
from product.routes import product_bp


app = Flask(__name__)
app.secret_key = 'secret_key'
init_db()


# реєстрація blueprint
app.register_blueprint(product_bp)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if company_exist(name):
            flash(f'Company {name} already exists!')
            return redirect(url_for('register'))
        else:
            # отримуємо хеш від паролю
            hash_pass = generate_password_hash(password)
            add_company(name, hash_pass)

            flash(f'Company {name} was created!')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if not company_exist(name):
            flash(f'Company {name} does not exist!')
            return redirect(url_for('login'))

        company = get_company_by_name(name)

        # перевіряємо хеш паролей, чи співпадають вони
        if not check_password_hash(company.password, password):
            flash(f'Password incorrect!')
            return redirect(url_for('login'))

        # в cookie файл зберігаємо назву компанії
        session['company'] = company.name

        flash(f'Welcome {name}!')
        return redirect(url_for('product.products'))

    return render_template('login.html')


app.run(debug=True)

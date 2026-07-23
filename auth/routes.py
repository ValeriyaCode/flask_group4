from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from actions_db import *
from werkzeug.security import generate_password_hash, check_password_hash

# створення Blueprint auth
auth_bp = Blueprint('auth', __name__, template_folder='templates')


def is_login_valid():
    pass

def is_password_valid():
    pass


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if company_exist(name):
            flash(f'Company {name} already exists!')
            return redirect(url_for('auth.register'))
        else:
            # отримуємо хеш від паролю
            hash_pass = generate_password_hash(password)
            add_company(name, hash_pass)

            flash(f'Company {name} was created!')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if not company_exist(name):
            flash(f'Company {name} does not exist!')
            return redirect(url_for('auth.login'))

        company = get_company_by_name(name)

        # перевіряємо хеш паролей, чи співпадають вони
        if not check_password_hash(company.password, password):
            flash(f'Password incorrect!')
            return redirect(url_for('auth.login'))

        # в cookie файл зберігаємо назву компанії
        session['company'] = company.name

        flash(f'Welcome {name}!')
        return redirect(url_for('product.products'))

    return render_template('auth/login.html')

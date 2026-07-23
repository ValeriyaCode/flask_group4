from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import init_db
from actions_db import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

# підключення до БД
init_db()


def is_logged():
    return 'company' in session

def current_company():
    name = session['company']
    return get_company_by_name(name)


@app.route('/', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def products():
    # для того, щоб дані в cookie не видалялись після закриття браузеру
    session.permanent = True

    if not is_logged():
        return redirect(url_for('login'))

    # отримуємо компанію
    company = current_company()
    print(company)

    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)

        if product_exists(title, company.id):
            flash(f'Product {title} already exists!')
        else:
            add_product(title, price, category, company.id)
            flash(f'Product {title} was added!')

        return redirect(url_for('products'))

    # актуальні категорії на основі товарів
    all_categories = get_categories(company.id)

    # обрана категорія
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_products = get_products(company.id)
    else:
        # фільтрація
        filter_products = get_products_by_category(choose_category, company.id)

    return render_template('product.html',
                           products=filter_products,
                           categories=all_categories,
                           choose_category=choose_category)


# динамічне посилання з параметрами <>
@app.route('/delete/<name_product>')
def delete(name_product):
    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('products'))


@app.route('/edit')
def edit():
    return render_template('edit.html')


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
        return redirect(url_for('products'))

    return render_template('login.html')


app.run(debug=True)

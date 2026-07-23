from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from actions_db import *

# створення Blueprint (логічного модулю)
product_bp = Blueprint('product', __name__, template_folder='templates')


def is_logged():
    return 'company' in session

def current_company():
    name = session['company']
    return get_company_by_name(name)


@product_bp.route('/', methods=['GET', 'POST'])
@product_bp.route('/products', methods=['GET', 'POST'])
def products():
    # для того, щоб дані в cookie не видалялись після закриття браузеру
    session.permanent = True

    if not is_logged():
        return redirect(url_for('auth.login'))

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

        return redirect(url_for('product.products'))

    # актуальні категорії на основі товарів
    all_categories = get_categories(company.id)

    # обрана категорія
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_products = get_products(company.id)
    else:
        # фільтрація
        filter_products = get_products_by_category(choose_category, company.id)

    return render_template('product/product.html',
                           products=filter_products,
                           categories=all_categories,
                           choose_category=choose_category)


# динамічне посилання з параметрами <>
@product_bp.route('/delete/<name_product>')
def delete(name_product):
    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('product.products'))


@product_bp.route('/edit')
def edit():
    return render_template('product/edit.html')
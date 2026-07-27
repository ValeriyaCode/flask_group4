from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

all_products = {}


@app.route('/', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)

        if title in all_products:
            flash(f'Product {title} already exists!')
        else:
            # додавання товару
            all_products.update({title: {'price': price, 'category': category}})
            flash(f'Product {title} was added!')

        return redirect(url_for('products'))

    return render_template('product.html', products=all_products)


# динамічне посилання з параметрами <>
@app.route('/delete/<name_product>')
def delete(name_product):
    all_products.pop(name_product)
    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('products'))


@app.route('/edit/<name_product>', methods=['GET', 'POST'])
def edit(name_product):
    current_price = all_products[name_product]['price']
    current_category = all_products[name_product]['category']

    if request.method == 'POST':
        new_category = request.form.get('category')
        new_price = request.form.get('price')

        new_price = float(new_price)

        if new_category == current_category and new_price == current_price:
            flash(f'Change data of this product!')
            return redirect(url_for('edit', name_product=name_product))

        all_products[name_product]['category'] = new_category
        all_products[name_product]['price'] = new_price

        flash(f'Product {name_product} was updated!')
        return redirect(url_for('products'))

    return render_template('edit.html',
                           name=name_product,
                           price=current_price,
                           category=current_category)

app.run(debug=True)



from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '***' # потрібен для flash-повідомлення


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')

        # flash - функція, для відправки повідомлення в межах наступного запиту
        flash(f'Hello, {name}!')

        # redirect - функція, яка перенаправляє на потрібну сторінку з методом GET
        # url_for - дозволяє посилатись на функцію, яка обробляє певний маршрут
        return redirect(url_for('index'))

    return render_template('index.html')


app.run(debug=True)

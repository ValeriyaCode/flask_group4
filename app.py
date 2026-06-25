from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # беремо дані з полей форми
        user_password = request.form.get('password')
        print(user_password)

    # беремо дані з адресного рядку
    user_request = request.args.get('search')
    return render_template('index.html', user_request=user_request)


app.run(debug=True)

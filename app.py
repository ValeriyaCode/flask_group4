from flask import Flask
from models import init_db

# імпортація blueprint
from product.routes import product_bp
from auth.routes import auth_bp

app = Flask(__name__)
app.secret_key = 'secret_key'
init_db()

# реєстрація blueprint
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)


app.run(debug=True)

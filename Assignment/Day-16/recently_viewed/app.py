from flask import Flask
from flask_cors import CORS
from blueprints.auth import auth_bp
from blueprints.products import products_bp

app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(products_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
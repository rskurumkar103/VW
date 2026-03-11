from flask import Flask
from products.routes import products_bp
from cart.routes import cart_bp
from orders.routes import orders_bp

app = Flask(__name__)

app.register_blueprint(products_bp)
app.register_blueprint(cart_bp, url_prefix="/cart")
app.register_blueprint(orders_bp, url_prefix="/orders")

if __name__ == "__main__":
    app.run(debug=True)
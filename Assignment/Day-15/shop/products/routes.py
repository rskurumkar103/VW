from flask import render_template, request, redirect, make_response
from . import products_bp
import json

# Dummy products
PRODUCTS = {
    "BED": 50000,
    "PILLOW": 500,
    "DESK": 1500,
    "LAMP": 2000,
    "CHAIR": 12000
}

@products_bp.route("/")
def product_list():
    return render_template("products.html", products=PRODUCTS)


@products_bp.route("/add/<product>")
def add_to_cart(product):
    cart = request.cookies.get("cart")

    if cart:
        cart = json.loads(cart)
    else:
        cart = {}

    cart[product] = cart.get(product, 0) + 1

    resp = make_response(redirect("/cart"))
    resp.set_cookie("cart", json.dumps(cart))

    return resp
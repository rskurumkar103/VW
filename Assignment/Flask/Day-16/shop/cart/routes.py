from flask import render_template, request, redirect, make_response
from . import cart_bp
import json

PRODUCTS = {
    "BED": 50000,
    "PILLOW": 500,
    "DESK": 1500,
    "LAMP": 2000,
    "CHAIR": 12000
}

@cart_bp.route("/")
def view_cart():
    cart = request.cookies.get("cart")

    if not cart:
        return render_template("cart.html", empty=True)

    cart = json.loads(cart)

    total = 0
    for item, qty in cart.items():
        total += PRODUCTS[item] * qty

    return render_template("cart.html", cart=cart, products=PRODUCTS, total=total)


@cart_bp.route("/update/<product>/<action>")
def update_cart(product, action):
    cart = request.cookies.get("cart")

    if not cart:
        return redirect("/cart")

    cart = json.loads(cart)

    if action == "increase":
        cart[product] += 1

    elif action == "decrease":
        cart[product] -= 1
        if cart[product] <= 0:
            del cart[product]

    resp = make_response(redirect("/cart"))

    if cart:
        resp.set_cookie("cart", json.dumps(cart))
    else:
        resp.delete_cookie("cart")

    return resp


@cart_bp.route("/clear")
def clear_cart():
    resp = make_response(redirect("/cart"))
    resp.delete_cookie("cart")
    return resp
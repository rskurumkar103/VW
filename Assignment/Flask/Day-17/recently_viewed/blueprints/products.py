from flask import Blueprint, request, jsonify, session, make_response

products_bp = Blueprint("products", __name__)

# Example product dataset
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200}
]

MAX_RECENT = 5

# API 2: Get All Products
@products_bp.route("/", methods=["GET"])
def get_all_products():
    return jsonify(PRODUCTS)


# API 3: View Product
@products_bp.route("/<int:product_id>", methods=["GET"])
def view_product(product_id):
    if "username" not in session:
        return jsonify({"error": "Login required"}), 401

    # Find product
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Manage recently viewed products in cookie
    resp = make_response(jsonify(product))
    recent = request.cookies.get("recent_products")
    if recent:
        recent_list = [int(i) for i in recent.split(",")]
    else:
        recent_list = []

    # Remove if already exists
    if product_id in recent_list:
        recent_list.remove(product_id)

    # Add to front
    recent_list.insert(0, product_id)

    # Keep maximum 5
    recent_list = recent_list[:MAX_RECENT]

    # Set cookie
    resp.set_cookie("recent_products", ",".join(map(str, recent_list)))

    return resp


# API 4: Get Recently Viewed Products
@products_bp.route("/recent", methods=["GET"])
def get_recent_products():
    recent = request.cookies.get("recent_products")
    if not recent:
        return jsonify([])

    recent_ids = [int(i) for i in recent.split(",")]
    recent_products = [p for pid in recent_ids for p in PRODUCTS if p["id"] == pid]

    # Return in order of recent_ids
    recent_products_sorted = sorted(
        recent_products, key=lambda x: recent_ids.index(x["id"])
    )

    # Only return id and name
    response = [{"id": p["id"], "name": p["name"]} for p in recent_products_sorted]

    return jsonify(response)
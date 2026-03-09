from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Adapter", "price": 2000},
    {"id": 4, "name": "Case", "price": 300}
]

# GET all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)


# POST new product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(new_product)

    return jsonify({
        "message": "Product added successfully",
        "product": new_product
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# In-memory storage
products = []

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Upload CSV endpoint
@app.route('/uploadproducts', methods=['POST'])
def upload_products():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    total_rows = 0
    products_added = 0
    failed_rows = 0

    with open(filepath, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            total_rows += 1

            name = row.get("name")
            price = row.get("price")
            stock = row.get("stock")

            try:

                if not name or name.strip() == "":
                    raise ValueError("Invalid name")

                price = float(price)
                stock = int(stock)

                if price <= 0:
                    raise ValueError("Invalid price")

                if stock < 0:
                    raise ValueError("Invalid stock")

                product = {
                    "name": name,
                    "price": price,
                    "stock": stock
                }

                products.append(product)
                products_added += 1

            except:
                failed_rows += 1

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    })


# View stored products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)
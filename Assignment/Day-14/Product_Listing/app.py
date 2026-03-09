from flask import Flask, render_template, request

app = Flask(__name__)

# Sample product data stored in memory
products = [
    {"name": "Laptop", "category": "Electronics", "price": 120000, "available": True},
    {"name": "Smartphone", "category": "Electronics", "price": 80000, "available": False},
    {"name": "Watch", "category": "Electronics", "price": 15000, "available": True},
    {"name": "Case", "category": "Accessories", "price": 3000, "available": False},
    {"name": "Cable", "category": "Accessories", "price": 2000, "available": True},

]

@app.route("/products")
def product_listing():
    filtered_products = products.copy()

    # Get query parameters
    category = request.args.get("category")
    availability = request.args.get("available")
    sort_price = request.args.get("sort")  # "low" or "high"

    # Filter by category
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]

    # Filter by availability
    if availability:
        if availability.lower() == "true":
            filtered_products = [p for p in filtered_products if p["available"]]
        elif availability.lower() == "false":
            filtered_products = [p for p in filtered_products if not p["available"]]

    # Sort by price
    if sort_price:
        reverse = True if sort_price.lower() == "high" else False
        filtered_products.sort(key=lambda x: x["price"], reverse=reverse)

    total_count = len(filtered_products)

    return render_template(
        "index.html",
        products=filtered_products,
        total_count=total_count,
        category=category,
        availability=availability,
        sort_price=sort_price
    )

if __name__ == "__main__":
    app.run(debug=True)
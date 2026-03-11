from . import orders_bp

@orders_bp.route("/")
def orders_home():
    return "Orders Page (Not implemented)"
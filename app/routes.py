
from flask import jsonify, request

from app.controllers.customer_controller import CustomerController


def register_routes(app):

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Northwind REST API is running!",
            "status": "success"
        }), 200

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy",
            "service": "Northwind REST API"
        }), 200

    # CREATE CUSTOMER
    @app.route("/api/customers", methods=["POST"])
    def create_customer():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Request body must be a JSON object"}), 400

        response, status_code = CustomerController.create_customer(data)
        return jsonify(response), status_code

    # GET ALL CUSTOMERS
    @app.route("/api/customers", methods=["GET"])
    def get_all_customers():
        response, status_code = CustomerController.get_all_customers()
        return jsonify(response), status_code

    # GET CUSTOMER BY ID
    @app.route("/api/customers/<customer_id>", methods=["GET"])
    def get_customer(customer_id):
        response, status_code = CustomerController.get_customer(customer_id)
        return jsonify(response), status_code

    # UPDATE CUSTOMER
    @app.route("/api/customers/<customer_id>", methods=["PUT"])
    def update_customer(customer_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Request body must be a JSON object"}), 400

        response, status_code = CustomerController.update_customer(
            customer_id, data
        )
        return jsonify(response), status_code

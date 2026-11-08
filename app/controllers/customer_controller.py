
from marshmallow import ValidationError

from app.schemas.customer_schema import CustomerSchema
from app.services.customer_service import CustomerService


class CustomerController:

    @staticmethod
    def create_customer(data):
        try:
            validated_data = CustomerSchema().load(data)
            customer = CustomerService.create_customer(validated_data)

            return {
                "message": "Customer created successfully",
                "customer_id": customer.customer_id
            }, 201

        except ValidationError as error:
            return {"errors": error.messages}, 400

    @staticmethod
    def get_all_customers():
        customers = CustomerService.get_all_customers()

        return {
            "customers": [
                customer.attribute_values
                for customer in customers
            ]
        }, 200

    @staticmethod
    def get_customer(customer_id):
        customer = CustomerService.get_customer(customer_id)

        if customer is None:
            return {"error": "Customer not found"}, 404

        return customer.attribute_values, 200

    @staticmethod
    def update_customer(customer_id, data):
        try:
            # Validate only the fields supplied for the update.
            validated_data = CustomerSchema().load(
                data,
                partial=True
            )

            customer = CustomerService.update_customer(
                customer_id,
                validated_data
            )

            if customer is None:
                return {"error": "Customer not found"}, 404

            return {
                "message": "Customer updated successfully",
                "customer_id": customer.customer_id
            }, 200

        except ValidationError as error:
            return {"errors": error.messages}, 400

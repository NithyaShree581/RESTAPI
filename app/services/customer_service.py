
from app.models.customer import Customer


class CustomerService:

    @staticmethod
    def create_customer(data):
        customer = Customer(**data)
        customer.save()
        return customer

    @staticmethod
    def get_all_customers():
        return list(Customer.scan())

    @staticmethod
    def get_customer(customer_id):
        try:
            return Customer.get(customer_id)
        except Customer.DoesNotExist:
            return None

    @staticmethod
    def update_customer(customer_id, data):
        customer = CustomerService.get_customer(customer_id)

        if customer is None:
            return None

        for key, value in data.items():
            if key != "customer_id":
                setattr(customer, key, value)

        customer.save()
        return customer

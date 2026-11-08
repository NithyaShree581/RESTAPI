
import os

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Customer(Model):
    class Meta:
        table_name = os.getenv("CUSTOMERS_TABLE", "NorthwindCustomers")
        region = os.getenv("AWS_REGION", "ap-south-1")

        endpoint = os.getenv("DYNAMODB_ENDPOINT")
        if endpoint:
            host = endpoint

    customer_id = UnicodeAttribute(hash_key=True)
    company_name = UnicodeAttribute()
    contact_name = UnicodeAttribute(null=True)
    contact_title = UnicodeAttribute(null=True)
    address = UnicodeAttribute(null=True)
    city = UnicodeAttribute(null=True)
    region = UnicodeAttribute(null=True)
    postal_code = UnicodeAttribute(null=True)
    country = UnicodeAttribute(null=True)
    phone = UnicodeAttribute(null=True)
    fax = UnicodeAttribute(null=True)

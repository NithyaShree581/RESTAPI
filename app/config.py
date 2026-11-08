
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "local-development-key")

    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

    CUSTOMERS_TABLE = os.getenv(
        "CUSTOMERS_TABLE", "NorthwindCustomers"
    )

    PRODUCTS_TABLE = os.getenv(
        "PRODUCTS_TABLE", "NorthwindProducts"
    )

    ORDERS_TABLE = os.getenv(
        "ORDERS_TABLE", "NorthwindOrders"
    )

    DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")

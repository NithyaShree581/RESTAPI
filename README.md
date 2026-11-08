# Northwind REST API

A RESTful API developed using **Python and Flask** to manage Northwind database operations. The application follows a modular MVC architecture, separating models, controllers, services, and validation schemas for better maintainability.

## Features

- Customer management – Create, retrieve, and update customer records.
- Product management – Designed to support product operations.
- Order management – Designed to support order operations.
- Customer order history – Designed to retrieve orders associated with a specific customer.
- Input validation using Marshmallow.
- Database mapping using PynamoDB.
- Modular MVC-style architecture.

## Technology Stack

- Python
- Flask
- PynamoDB
- Boto3
- Marshmallow
- Pytest
- Moto
- python-dotenv

## Project Structure

```text
RESTAPI/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── __init__.py
│   ├── config.py
│   └── routes.py
│
├── data/
├── scripts/
├── tests/
│   ├── unit/
│   └── integration/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

## API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/health` | Check application health |

### Customer Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/customers` | Create a customer |
| GET | `/api/customers` | Retrieve all customers |
| GET | `/api/customers/<customer_id>` | Retrieve a customer by ID |
| PUT | `/api/customers/<customer_id>` | Update customer details |

## Sample Customer Request

**POST** `/api/customers`

```json
{
    "customer_id": "ALFKI",
    "company_name": "Alfreds Futterkiste",
    "contact_name": "Maria Anders",
    "city": "Berlin",
    "country": "Germany"
}
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/NithyaShree581/RESTAPI.git
cd RESTAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file using `.env.example` and configure the required environment variables.

### 6. Run the application

```bash
python run.py
```

The API runs locally at:

`http://127.0.0.1:5000`

## Architecture

The application follows an MVC-style architecture:

- **Models:** Define the structure of customer, product, and order data.
- **Controllers:** Handle incoming API requests and responses.
- **Services:** Manage business logic and database operations.
- **Schemas:** Validate incoming request data.
- **Routes:** Define API endpoints and connect them to controllers.

## AWS Deployment

The proposed deployment architecture uses:

- **AWS API Gateway** – Handles incoming API requests.
- **AWS Lambda** – Executes the Flask application.
- **Amazon DynamoDB** – Provides database persistence.
- **Amazon CloudWatch** – Handles application logging and monitoring.

AWS deployment and live DynamoDB integration could not be completed because AWS credentials and account access were unavailable during development. The Flask application was developed locally.

## Author

Developed as part of a REST API development assignment.

**GitHub Repository:** https://github.com/NithyaShree581/RESTAPI

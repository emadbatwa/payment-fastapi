# Payment Gateway Integration

A FastAPI-based payment gateway integration service that supports multiple payment methods (PayPal, Apple Pay) using SOLID principles and the Factory pattern.

## Features

- Multiple payment method support (PayPal, Apple Pay)
- Clean architecture using SOLID principles
- Factory pattern for payment service creation
- Async/await support
- Request/Response validation using Pydantic
- Type hints and modern Python practices


## Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emadbatwa/payment-fastapi
cd payment-fastapi
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Running the Application

1. Start the FastAPI server:
```bash
fastapi dev
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Process Payment
- **URL**: `/api/pay`
- **Method**: `POST`
- **Request Body**:
```json
{
    "price": 99.99,
    "method": "paypal"  // or "applepay"
}
```
- **Response**:
```json
{
    "transaction_id": "PP-uuid-here"
}
```

## Usage Example

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.post(
        "http://localhost:8000/api/pay",
        json={
            "price": 99.99,
            "method": "paypal"
        }
    )
    print(response.json())
```

## Architecture

### SOLID Principles Implementation

1. **Single Responsibility Principle (SRP)**
   - Each service class handles only one payment method
   - Clear separation of concerns between request/response models

2. **Open/Closed Principle (OCP)**
   - New payment methods can be added without modifying existing code
   - Factory pattern allows for easy extension

3. **Liskov Substitution Principle (LSP)**
   - All payment services implement the same interface
   - Services can be used interchangeably

4. **Interface Segregation Principle (ISP)**
   - Clean, focused interface for payment services
   - No unnecessary method dependencies

5. **Dependency Inversion Principle (DIP)**
   - High-level modules depend on abstractions
   - Factory creates concrete implementations

### Factory Pattern

The `PaymentServiceFactory` creates the appropriate payment service based on the payment method:

```python
@app.post("/api/pay", response_model=PaymentResponse)
async def process_payment(payment_request: PaymentRequest):
    payment_service = PaymentServiceFactory.create(payment_request.method)
    transaction_id = await payment_service.checkout(payment_request.price)
    return PaymentResponse(transaction_id=transaction_id)
```


## Acknowledgments

- FastAPI framework
- Pydantic for data validation
- Python typing for type hints
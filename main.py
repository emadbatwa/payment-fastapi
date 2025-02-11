from sys import prefix

from models.db import create_db_and_tables, SessionDep
from models.transaction import Transaction
from schemas.payment_request import PaymentRequest
from schemas.payment_response import PaymentResponse
from factories.payment_service_factory import PaymentServiceFactory
from typing import Annotated
from fastapi import FastAPI, Query, APIRouter
from sqlmodel import select
from services.transaction_service import TransactionService
from services.payment_service import PaymentService


router = APIRouter(prefix="/api")
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@router.post("pay", response_model=PaymentResponse)
async def process_payment(payment_request: PaymentRequest, session: SessionDep):
    return await PaymentService.process_payment_(payment_request, session)

@router.get("transaction")
def get_transactions(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[PaymentResponse]:
    transactions = session.exec(select(Transaction).offset(offset).limit(limit)).all()
    return transactions

app.include_router(router)

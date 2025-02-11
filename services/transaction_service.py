from models.db import SessionDep
from models.transaction import Transaction


class TransactionService:
    @staticmethod
    async def store(transaction: Transaction, session: SessionDep):
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction


from sqlmodel import Field, SQLModel

class Transaction(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    method: str
    price: int

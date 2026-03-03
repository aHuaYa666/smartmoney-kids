from pydantic import BaseModel

class TransactionBase(BaseModel):
    item_name: str
    amount: float
    type: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    class Config:
        from_attributes = True
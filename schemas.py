from pydantic import BaseModel, Field, validator

class TransactionBase(BaseModel):
    item_name: str
    amount: float = Field(..., gt=0, description="The amount must be greater than zero")
    type: str # 'save' or 'spend'

    @validator('type')
    def validate_type(cls, v):
        if v.lower() not in ['save', 'spend']:
            raise ValueError('Type must be either "save" or "spend"')
        return v.lower()

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        from_attributes = True

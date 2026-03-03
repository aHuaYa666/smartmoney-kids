from sqlalchemy import Column, Integer, String, Float
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    amount = Column(Float)
    type = Column(String) # "save" or "spend"
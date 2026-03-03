from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

# Initialize Database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SmartMoney Kids API", version="1.1.0")

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartMoney Kids Backend", "status": "Active"}

@app.post("/transactions/", response_model=schemas.Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    # Business Logic: Check if spending exceeds balance
    if transaction.type.lower() == "spend":
        current_balance = get_total_balance(db)["current_balance"]
        if transaction.amount > current_balance:
            raise HTTPException(
                status_code=400, 
                detail=f"Insufficient funds. Current balance is {current_balance}"
            )
    
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
@app.get("/transactions/", response_model=List[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Transaction).offset(skip).limit(limit).all()

@app.get("/balance/")
def get_total_balance(db: Session = Depends(get_db)):
    """
    Business Logic: Automatically calculates the net balance 
    by subtracting 'spend' from 'save' entries.
    """
    transactions = db.query(models.Transaction).all()
    total_save = sum(t.amount for t in transactions if t.type.lower() == "save")
    total_spend = sum(t.amount for t in transactions if t.type.lower() == "spend")
    
    return {
        "total_deposited": total_save,
        "total_withdrawn": total_spend,
        "current_balance": total_save - total_spend,
        "currency": "USD"
    }



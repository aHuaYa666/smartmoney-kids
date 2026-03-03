# 📚 SmartMoney Kids - Technical Documentation

This directory contains the technical specifications and logic flows for the SmartMoney Kids Backend.

## 🏗️ Backend Architecture
The system is built using **FastAPI** (Asynchronous Server Gateway Interface) and **SQLAlchemy ORM** for structured data persistence in **SQLite**.

## ⚙️ Automated Business Logic
To ensure financial accuracy for young users, the following automated rules are enforced at the API level:

### 1. Real-Time Balance Aggregation
The `/balance/` endpoint automatically calculates the user's net worth by:
- **Summing** all entries where `type == "save"`.
- **Subtracting** all entries where `type == "spend"`.
- **Filtering** invalid or zero-sum transactions through Pydantic schemas.

### 2. Overdraft Protection (Error Handling)
The system prevents "Spending what you don't have." 
- If a `POST /transactions/` request is sent with `type: spend` and an `amount` greater than the current balance, the server returns a **400 Bad Request** with a custom error message.

## 🧪 Automated Testing (Quality Assurance)
Reliability is verified using **Pytest**.
- **Test Suite**: `test_main.py`
- **Scenarios Covered**: Successful deposits, successful withdrawals, and blocked overdraft attempts.

---
*Maintained by aHuaYa666 - Updated March 3, 2026*

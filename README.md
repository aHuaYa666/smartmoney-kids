# SmartMoney Kids 🐣💰

**SmartMoney Kids** is a functional MVP designed to make financial literacy interactive and safe for children. Originally conceived during a Devpost hackathon, the project now features a **robust RESTful API backend** to handle real-time transaction logging and automated balance management.

## 🚀 Status: MVP Backend Live (Updated March 3)
The core backend architecture is complete and fully functional, featuring automated business logic for financial calculations.

## 🛠️ Technical Improvements (March 3 Update)
- **Automated Calculations**: Added a `/balance/` endpoint that performs server-side aggregation of financial data (Save vs. Spend).
- **Strict Data Validation**: Implemented Pydantic validators to ensure data integrity (preventing negative amounts or invalid transaction types).
- **RESTful Best Practices**: Standardized response models and utilized FastAPI's dependency injection for database sessions.

## ✨ Implemented Features
* **Transaction Automation**: Built-in logic to handle "Save" vs "Spend" activities.
* **Data Integrity**: Used Pydantic schemas to ensure all financial inputs are validated.
* **Relational Database**: Implemented SQLAlchemy with SQLite for reliable data persistence.
* **Interactive API Docs**: Integrated Swagger UI for real-time testing and debugging.

## 🛠️ Tech Stack
* **Backend**: Python 3.11+ (FastAPI)
* **Database**: SQLite (SQLAlchemy ORM)
* **Testing**: Swagger UI / Postman

## 🏁 Quick Start (For Recruiters/Developers)
1. **Clone the repo**: `git clone https://github.com/aHuaYa666/smartmoney-kids.git`
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run the server**: `uvicorn main:app --reload`
4. **Explore the API**: Open `http://127.0.0.1:8000/docs` to interact with the endpoints.

### 🧪 Run Automated Tests
To verify the business logic (Balance calculation & Overdraft protection):
```bash
pytest
```

## 🌟 Why This Project?
Financial automation isn't just for adults. This project demonstrates my ability to build secure, scalable backend systems that simplify complex data workflows—skills I am eager to bring to the **Technology Automation** team at BCD Travel.

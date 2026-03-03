from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_balance_calculation():
    # 1. Deposit $100
    client.post("/transactions/", json={"item_name": "Allowance", "amount": 100, "type": "save"})
    # 2. Spend $30
    client.post("/transactions/", json={"item_name": "Toy", "amount": 30, "type": "spend"})
    
    # 3. Check if balance is exactly $70
    response = client.get("/balance/")
    assert response.status_code == 200
    assert response.json()["current_balance"] == 70.0

def test_insufficient_funds():
    # Try to spend more than available
    response = client.post("/transactions/", json={"item_name": "Ferrari", "amount": 9999, "type": "spend"})
    assert response.status_code == 400
    assert "Insufficient funds" in response.json()["detail"]
from fastapi import APIRouter
from pydantic import BaseModel
from app.db import insert_purchase
import sqlite3

router = APIRouter()

class PurchaseRequest(BaseModel):
    user_id: str
    amount: float

@router.post("/purchase")
def purchase_gold(request: PurchaseRequest):
    grams = request.amount / 6000  # Assume gold price ₹6000 per gram
    insert_purchase(request.user_id, request.amount, grams)
    
    return {
        "message": "Purchase successful!",
        "user_id": request.user_id,
        "amount": request.amount,
        "grams": grams,
        "status": "confirmed"
    }

@router.get("/purchases")
def get_purchases(user_id: str = None):
    conn = sqlite3.connect("gold.db")
    cursor = conn.cursor()

    if user_id:
        cursor.execute("SELECT * FROM purchases WHERE user_id = ?", (user_id,))
    else:
        cursor.execute("SELECT * FROM purchases")

    rows = cursor.fetchall()
    conn.close()

    purchases = []
    for row in rows:
        purchases.append({
            "id": row[0],
            "user_id": row[1],
            "amount": row[2],
            "grams": row[3],
            "timestamp": row[4]
        })
    
    return {"purchases": purchases}

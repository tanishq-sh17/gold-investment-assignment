from fastapi import APIRouter
from pydantic import BaseModel
from app.db import insert_purchase

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

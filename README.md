# 💰 Kuber AI Gold Investment Workflow (Assignment)

This project emulates **Simplify Money App’s Kuber AI workflow** for gold investment.

## 🚀 Features
1. **API 1 - Chatbot (DeepSeek)**  
   - Interacts with users about gold investment.  
   - Uses **DeepSeek LLM via OpenRouter**.  
   - Nudges users to buy digital gold.

2. **API 2 - Purchase API**  
   - Handles gold purchases.  
   - Records user purchases in SQLite.  
   - Returns success confirmation.

---

## 📂 Project Structure
gold-investment-assignment/
── app/
   ── main.py          
   ── api1_chat.py    
   ── api2_purchase.py
   ── db.py           
── requirements.txt
── README.md



---

## ⚡ Setup Instructions


### 1️⃣ Clone Repository
```bash
git clone https://github.com/tanishq-sh17/gold-investment-assignment.git
cd gold-investment-assignment
### 2️⃣ Install Dependencies
pip install -r requirements.txt
### 3️⃣ Setup Environment Variables
Create a .env file in the project root:
OPENROUTER_API_KEY=your_openrouter_api_key_here
### 4️⃣ Run the Server
uvicorn app.main:app --reload
Server will start at:
👉 http://127.0.0.1:8000

##🔑 API Endpoints
Chatbot API (API 1)

   - POST /api1/chat → Ask about gold investment

Purchase API (API 2)

  - POST /api2/purchase → Buy gold

  - GET /api2/purchases → View all purchases

  - GET /api2/purchases?user_id=<id> → View purchases by user




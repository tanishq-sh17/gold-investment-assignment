# Kuber AI Gold Investment Workflow

This project emulates Simplify Money App's Kuber AI workflow for gold investment.

## Features

### 1. API 1 - Chatbot (Rule-Based / LLM via OpenRouter)
- Interacts with users about gold investment
- Can work with rule-based intent detection or DeepSeek LLM via OpenRouter
- Nudges users to buy digital gold

### 2. API 2 - Purchase API
- Handles gold purchases
- Records user purchases in SQLite
- Returns success confirmation
- Provides an endpoint to view purchase history

## Project Structure

```
gold-investment-assignment/
├── app/
│   ├── main.py              # Entry point
│   ├── api1_chat.py         # Chatbot API
│   ├── api2_purchase.py     # Purchase API
│   └── db.py                # SQLite database utils
├── requirements.txt
├── README.md
└── .env.example             # Example env file (no real keys)
```

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/tanishq-sh17/gold-investment-assignment.git
cd gold-investment-assignment
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Run the Server
```bash
uvicorn app.main:app --reload
```

- Server will start at: `http://127.0.0.1:8000`
- Swagger UI loads at `/` by default

## API Endpoints

### Chatbot API (API 1)
- **POST** `/api1/chat` → Ask about gold investment

### Purchase API (API 2)
- **POST** `/api2/purchase` → Buy gold
- **GET** `/api2/purchases` → View all purchases
- **GET** `/api2/purchases?user_id=<user_id>` → View purchases by user

## Deployment

This project can be deployed on Render Free Tier or any cloud service supporting FastAPI.

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLite** - Lightweight database for storing purchase records
- **OpenRouter** - API gateway for accessing various LLMs
- **DeepSeek LLM** - Language model for intelligent chat responses
- **Uvicorn** - ASGI server for running FastAPI applications

## License

This project is created as an assignment to demonstrate gold investment workflow implementation.

## Contributing

Feel free to fork this repository and submit pull requests for improvements.

## Support

If you encounter any issues or have questions, please create an issue in the GitHub repository.

  - GET /api2/purchases → View all purchases

  - GET /api2/purchases?user_id=<id> → View purchases by user




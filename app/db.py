import sqlite3

def init_db():
    conn = sqlite3.connect("gold.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            amount REAL,
            grams REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_purchase(user_id, amount, grams):
    conn = sqlite3.connect("gold.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO purchases (user_id, amount, grams) VALUES (?, ?, ?)",
                   (user_id, amount, grams))
    conn.commit()
    conn.close()

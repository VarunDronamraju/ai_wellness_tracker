import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "tracker.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted_timestamp TEXT NOT NULL
        )
    """)
    return conn

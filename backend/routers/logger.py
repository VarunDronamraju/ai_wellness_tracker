from fastapi import APIRouter
from datetime import datetime
from backend.core.db import get_db_connection
from backend.core.security import encrypt_data

router = APIRouter()

@router.get("/")
def log_screen_time():
    timestamp = datetime.utcnow().isoformat()
    encrypted = encrypt_data(timestamp)

    conn = get_db_connection()
    conn.execute("INSERT INTO logs (encrypted_timestamp) VALUES (?)", (encrypted,))
    conn.commit()
    conn.close()

    return {"screen_time": "2h 17m", "logged": True}

import sqlite3
from backend.core.db import DB_PATH

def delete_logs():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM logs")
    conn.commit()
    conn.close()
    print("All logs deleted.")

if __name__ == "__main__":
    delete_logs()

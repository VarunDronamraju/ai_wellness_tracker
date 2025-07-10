import sqlite3
import json
from backend.core.db import DB_PATH
from backend.core.security import decrypt_data
from pathlib import Path

def export_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_timestamp FROM logs")
    rows = cursor.fetchall()
    conn.close()

    logs = [decrypt_data(row[0]) for row in rows]

    output = {
        "logs": logs,
        "count": len(logs)
    }

    Path("exported_logs.json").write_text(json.dumps(output, indent=2))
    print(f"Exported {len(logs)} records to exported_logs.json")

if __name__ == "__main__":
    export_logs()

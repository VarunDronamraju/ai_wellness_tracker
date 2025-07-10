from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/sync")
def sync_to_cloud():
    # Simulated upload to cloud
    summary = {
        "total_screen_time_today": f"{random.randint(1, 4)}h {random.randint(0, 59)}m",
        "synced": True,
        "provider": "AWS S3 (Simulated)"
    }
    return summary

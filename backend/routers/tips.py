from fastapi import APIRouter
import random

router = APIRouter()

TIPS = [
    "Adjust your posture regularly.",
    "Take a break every 30 minutes.",
    "Blink to avoid eye strain.",
    "Stretch your shoulders.",
    "Breathe deeply for 60 seconds."
]

@router.get("/")
def get_tip():
    return {"tip": random.choice(TIPS)}

from fastapi import APIRouter
import random

router = APIRouter()

TIPS = [
    "Take regular screen breaks every 30 minutes.",
    "Keep your back straight and shoulders relaxed.",
    "Stay hydrated throughout the day.",
    "Try a 5-minute stretch every hour.",
    "Blink often to reduce eye strain."
]

@router.get("/")
def get_tip():
    return {"tip": random.choice(TIPS)}

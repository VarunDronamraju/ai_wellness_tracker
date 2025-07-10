from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/")
def get_posture_status():
    return {"posture": random.choice(["Good", "Bad"])}

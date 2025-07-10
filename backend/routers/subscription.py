from fastapi import APIRouter

router = APIRouter()

subscription_state = {"enabled": True}

@router.get("/status")
def get_subscription_status():
    return {"premium": subscription_state["enabled"]}

@router.post("/toggle")
def toggle_subscription():
    subscription_state["enabled"] = not subscription_state["enabled"]
    return {"premium": subscription_state["enabled"]}

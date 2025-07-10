import requests

def fetch_tip():
    try:
        res = requests.get("http://127.0.0.1:8000/tip", timeout=3)
        return res.json().get("tip", "No tip available.")
    except:
        return "Error fetching tip."

def get_premium_status():
    try:
        res = requests.get("http://127.0.0.1:8000/subscription/status", timeout=3)
        return res.json().get("premium", False)
    except:
        return False

def toggle_premium():
    try:
        res = requests.post("http://127.0.0.1:8000/subscription/toggle", timeout=3)
        return res.json().get("premium", False)
    except:
        return False

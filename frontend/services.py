import requests

def safe_get(url):
    try:
        res = requests.get(url, timeout=3)
        return res.json()
    except:
        return {}

def get_screen_time():
    res = safe_get("http://127.0.0.1:8000/log")
    return res.get("screen_time", "0h 0m")

def get_tip_of_the_day():
    res = safe_get("http://127.0.0.1:8000/tip")
    return res.get("tip", "Stay hydrated!")

def toggle_premium():
    try:
        res = requests.post("http://127.0.0.1:8000/subscription/toggle", timeout=3)
        return res.json().get("premium", False)
    except:
        return False

def get_premium_status():
    res = safe_get("http://127.0.0.1:8000/subscription/status")
    return res.get("premium", False)

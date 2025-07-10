from fastapi import FastAPI
from backend.routers import logger, tips, posture
from backend.routers import logger, tips, posture, sync, subscription
app = FastAPI()
app.include_router(sync.router, prefix="/cloud", tags=["Cloud"])
app.include_router(subscription.router, prefix="/subscription", tags=["Subscription"])



app.include_router(logger.router, prefix="/log", tags=["Logger"])
app.include_router(tips.router, prefix="/tip", tags=["Tips"])
app.include_router(posture.router, prefix="/posture", tags=["Posture"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

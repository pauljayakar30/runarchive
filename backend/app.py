from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.strava import AUTH_URL, exchange_code_for_token

from backend.crud import save_activities

from backend.strava import (
    AUTH_URL,
    exchange_code_for_token,
    get_activities
)

app = FastAPI(
    title="RunArchive",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "RunArchive",
        "status": "running"
    }

@app.get("/connect-strava")
def connect_strava():
    return RedirectResponse(AUTH_URL)

@app.get("/callback")
def callback(code: str):
    token_data = exchange_code_for_token(code)

    access_token = token_data["access_token"]

    activities = get_activities(access_token)

    save_activities(activities)

    return {
        "message": "Activities synced",
        "count": len(activities)
    }
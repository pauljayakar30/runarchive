from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.strava import AUTH_URL, exchange_code_for_token

from backend.crud import save_activities

from backend.analytics.summary import get_summary

from backend.strava import (
    AUTH_URL,
    exchange_code_for_token,
    get_activities
)

from backend.analytics.monthly import (
    get_monthly_summary
)

from backend.analytics.weekly import (
    get_weekly_summary
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

@app.get("/analytics/summary")
def analytics_summary():
    return get_summary()

@app.get("/analytics/monthly")
def monthly_summary():
    return get_monthly_summary()

@app.get("/analytics/weekly")
def weekly_summary():
    return get_weekly_summary()
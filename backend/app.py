from fastapi import FastAPI
from fastapi.responses import RedirectResponse
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

from backend.reports.daily import (
    get_daily_report
)

from backend.reports.monthly import (
    get_monthly_report
)

from backend.reports.comparison import (
    compare_months
)

from backend.analytics.dashboard import (
    get_dashboard
)

from backend.crud_athlete import save_athlete

from backend.services.token_service import (
    get_valid_access_token
)

import os

from backend.database import SessionLocal
from backend.models import Activity, Athlete

from backend.services.scheduler import (
    scheduler
)

from backend.services.telegram_service import (
    send_telegram_message
)

from backend.services.telegram_report_job import (
    monthly_report_job
)

app = FastAPI(
    title="RunArchive"
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

    save_athlete(token_data)

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

@app.get("/reports/day/{target_date}")
def daily_report(target_date: str):

    return get_daily_report(
        target_date
    )

@app.get(
    "/reports/month/{year}/{month}"
)
def monthly_report(
    year: int,
    month: int
):
    return get_monthly_report(
        year,
        month
    )   

@app.get(
    "/reports/compare/"
    "{year1}/{month1}/"
    "{year2}/{month2}"
)
def compare_report(
    year1: int,
    month1: int,
    year2: int,
    month2: int
):
    return compare_months(
        year1,
        month1,
        year2,
        month2
    )

@app.get("/dashboard")
def dashboard():

@app.get("/dashboard")
def dashboard():

    return get_dashboard()


@app.post("/sync")
def sync_activities():

    token = get_valid_access_token()

    activities = get_activities(token)

    save_activities(activities)

    return {
        "message": "Sync completed",
        "count": len(activities)
    }
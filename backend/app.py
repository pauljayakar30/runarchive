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

from backend.reports.daily import (
    get_daily_report
)

from backend.reports.monthly import (
    get_monthly_report
)

from backend.reports.insights import (
    compare_months
)

from backend.reports.email import (
    generate_monthly_email
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

@app.get(
    "/reports/email/"
    "{year}/{month}/"
    "{previous_year}/{previous_month}"
)
def monthly_email(
    year: int,
    month: int,
    previous_year: int,
    previous_month: int
):

    return generate_monthly_email(
        year,
        month,
        previous_year,
        previous_month
    )
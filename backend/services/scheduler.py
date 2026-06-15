from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from backend.services.token_service import (
    get_valid_access_token
)

from backend.strava import get_activities
from backend.crud import save_activities


def daily_sync():

    try:

        print("Starting scheduled sync...")

        token = get_valid_access_token()

        activities = get_activities(token)

        save_activities(activities)

        print(
            f"Sync complete: {len(activities)} activities"
        )

    except Exception as e:

        print(
            f"Sync failed: {e}"
        )


scheduler = BackgroundScheduler()

scheduler.add_job(
    daily_sync,
    "cron",
    hour=6,
    minute=0
)
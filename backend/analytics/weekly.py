from collections import defaultdict
from datetime import datetime

from backend.database import SessionLocal
from backend.models import Activity


def get_weekly_summary():
    db = SessionLocal()

    try:
        activities = db.query(Activity).all()

        weekly_data = defaultdict(
            lambda: {
                "runs": 0,
                "distance_km": 0
            }
        )

        for activity in activities:

            date = datetime.fromisoformat(
                activity.date
            )

            year, week, _ = date.isocalendar()

            week_key = f"{year}-W{week}"

            weekly_data[week_key]["runs"] += 1

            weekly_data[week_key]["distance_km"] += (
                activity.distance_m / 1000
            )

        return {
            week: {
                "runs": value["runs"],
                "distance_km": round(
                    value["distance_km"],
                    2
                )
            }
            for week, value in weekly_data.items()
        }

    finally:
        db.close()
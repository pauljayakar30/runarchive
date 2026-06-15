from collections import defaultdict
from datetime import datetime

from backend.database import SessionLocal
from backend.models import Activity


def get_monthly_summary():
    db = SessionLocal()

    try:
        activities = db.query(Activity).all()

        monthly_data = defaultdict(
            lambda: {
                "runs": 0,
                "distance_km": 0
            }
        )

        for activity in activities:

            date = datetime.fromisoformat(
                activity.date
            )

            month_key = date.strftime(
                "%Y-%m"
            )

            monthly_data[month_key]["runs"] += 1

            monthly_data[month_key][
                "distance_km"
            ] += (
                activity.distance_m / 1000
            )

        return {
            month: {
                "runs": value["runs"],
                "distance_km": round(
                    value["distance_km"],
                    2
                )
            }
            for month, value in monthly_data.items()
        }

    finally:
        db.close()
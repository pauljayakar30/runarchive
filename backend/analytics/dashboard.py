from backend.analytics.summary import get_summary
from backend.analytics.monthly import get_monthly_summary

from backend.database import SessionLocal
from backend.models import Activity, Athlete


def get_dashboard():

    db = SessionLocal()

    try:

        activity_count = db.query(
            Activity
        ).count()

        athlete_count = db.query(
            Athlete
        ).count()

        latest_activity = (
            db.query(Activity)
            .order_by(
                Activity.date.desc()
            )
            .first()
        )

        return {
            "summary": get_summary(),
            "monthly": get_monthly_summary(),
            "athletes": athlete_count,
            "activities": activity_count,
            "latest_activity":
                latest_activity.date
                if latest_activity
                else None
        }

    finally:

        db.close()
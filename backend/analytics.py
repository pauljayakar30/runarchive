from backend.database import SessionLocal
from backend.models import Activity


def get_summary():
    db = SessionLocal()

    try:
        activities = db.query(Activity).all()

        total_runs = len(activities)

        total_distance_m = sum(
            a.distance_m for a in activities
        )

        longest_run_m = max(
            (a.distance_m for a in activities),
            default=0
        )

        avg_distance_m = (
            total_distance_m / total_runs
            if total_runs
            else 0
        )

        return {
            "total_runs": total_runs,
            "total_distance_km": round(
                total_distance_m / 1000,
                2
            ),
            "longest_run_km": round(
                longest_run_m / 1000,
                2
            ),
            "average_run_km": round(
                avg_distance_m / 1000,
                2
            )
        }

    finally:
        db.close()
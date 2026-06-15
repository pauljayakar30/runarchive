from backend.analytics.repository import get_all_activities
from backend.reports.helpers import km, hours


def get_monthly_report(year: int, month: int):

    activities = get_all_activities()

    target_month = f"{year}-{month:02d}"

    monthly_activities = [
        activity
        for activity in activities
        if activity.date.startswith(target_month)
    ]

    if not monthly_activities:
        return {
            "month": target_month,
            "message": "No activities found"
        }

    total_runs = len(monthly_activities)

    total_distance_m = sum(
        a.distance_m
        for a in monthly_activities
    )

    total_time_s = sum(
        a.moving_time_s
        for a in monthly_activities
    )

    longest_run_m = max(
        a.distance_m
        for a in monthly_activities
    )

    avg_distance_m = (
        total_distance_m / total_runs
    )

    return {
        "month": target_month,
        "total_runs": total_runs,
        "total_distance_km": km(total_distance_m),
        "average_run_km": km(avg_distance_m),
        "longest_run_km": km(longest_run_m),
        "total_time_hours": hours(total_time_s)
    }
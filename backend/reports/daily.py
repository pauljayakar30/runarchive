from datetime import date

from backend.analytics.repository import (
    get_all_activities
)


def get_daily_report(target_date: str):

    activities = get_all_activities()

    matching = []

    total_distance = 0

    for activity in activities:

        activity_date = (
            activity.date[:10]
        )

        if activity_date == target_date:

            matching.append({
                "name": activity.name,
                "distance_km": round(
                    activity.distance_m / 1000,
                    2
                ),
                "moving_time_min": round(
                    activity.moving_time_s / 60,
                    1
                )
            })

            total_distance += (
                activity.distance_m / 1000
            )

    return {
        "date": target_date,
        "activities": matching,
        "total_distance_km": round(
            total_distance,
            2
        )
    }
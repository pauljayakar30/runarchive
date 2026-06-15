import json

from backend.database import SessionLocal
from backend.models import Activity


def save_activity(activity_data):
    db = SessionLocal()

    try:
        existing = (
            db.query(Activity)
            .filter(
                Activity.strava_id == activity_data["id"]
            )
            .first()
        )

        if existing:
            return

        activity = Activity(
            strava_id=activity_data["id"],
            name=activity_data["name"],
            date=activity_data["start_date_local"],
            sport_type=activity_data["sport_type"],
            distance_m=activity_data["distance"],
            moving_time_s=activity_data["moving_time"],
            average_speed=activity_data.get("average_speed"),
            elevation_gain=activity_data.get(
                "total_elevation_gain"
            ),
            raw_json=json.dumps(activity_data)
        )
        print(
    "Inserting activity:",
    activity_data["id"]
)
        db.add(activity)
        db.commit()

    finally:
        db.close()

    

def save_activities(activities):
    for activity in activities:
        save_activity(activity)

def save_activities(activities):
    print(f"Received {len(activities)} activities")

    for activity in activities:
        print(
            "Saving:",
            activity["name"]
        )

        save_activity(activity)
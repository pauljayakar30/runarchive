from backend.database import SessionLocal
from backend.models import Activity

db = SessionLocal()

count = db.query(Activity).count()

print("COUNT =", count)

activities = db.query(Activity).limit(5).all()

for activity in activities:
    print(
        activity.strava_id,
        activity.name
    )

db.close()
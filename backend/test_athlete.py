from backend.database import SessionLocal
from backend.models import Athlete

db = SessionLocal()

athletes = db.query(Athlete).all()

print("ATHLETES FOUND:", len(athletes))

for athlete in athletes:
    print("ID:", athlete.strava_id)

db.close()
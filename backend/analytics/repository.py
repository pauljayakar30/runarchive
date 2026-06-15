from backend.database import SessionLocal
from backend.models import Activity


def get_all_activities():
    db = SessionLocal()

    try:
        return db.query(Activity).all()

    finally:
        db.close()
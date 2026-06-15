from backend.database import SessionLocal
from backend.models import Athlete


def save_athlete(token_data):

    db = SessionLocal()

    try:

        athlete_info = token_data["athlete"]

        athlete = (
            db.query(Athlete)
            .filter(
                Athlete.strava_id == athlete_info["id"]
            )
            .first()
        )

        if athlete:

            athlete.access_token = token_data["access_token"]
            athlete.refresh_token = token_data["refresh_token"]
            athlete.expires_at = token_data["expires_at"]

        else:

            athlete = Athlete(
                strava_id=athlete_info["id"],
                access_token=token_data["access_token"],
                refresh_token=token_data["refresh_token"],
                expires_at=token_data["expires_at"]
            )

            db.add(athlete)

        db.commit()

    finally:

        db.close()
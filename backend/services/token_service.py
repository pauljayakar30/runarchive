import time

from backend.database import SessionLocal
from backend.models import Athlete
from backend.strava import (
    refresh_access_token
)


def get_valid_access_token():

    db = SessionLocal()

    try:

        athlete = (
            db.query(Athlete)
            .first()
        )

        now = int(time.time())

        if athlete.expires_at > now:

            return athlete.access_token

        token_data = (
            refresh_access_token(
                athlete.refresh_token
            )
        )

        athlete.access_token = (
            token_data["access_token"]
        )

        athlete.refresh_token = (
            token_data["refresh_token"]
        )

        athlete.expires_at = (
            token_data["expires_at"]
        )

        db.commit()

        return athlete.access_token

    finally:

        db.close()
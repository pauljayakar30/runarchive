from datetime import datetime

from backend.database import SessionLocal
from backend.models import Activity


def get_streak():

    db = SessionLocal()

    try:

        activities = (
            db.query(Activity)
            .order_by(Activity.date.desc())
            .all()
        )

        if not activities:
            return {
                "current_streak_days": 0,
                "longest_streak_days": 0
            }

        dates = sorted(
            {
                datetime.strptime(
                    activity.date[:10],
                    "%Y-%m-%d"
                ).date()
                for activity in activities
            }
        )

        longest = 1
        current = 1

        for i in range(1, len(dates)):

            difference = (
                dates[i] - dates[i - 1]
            ).days

            if difference == 1:

                current += 1
                longest = max(
                    longest,
                    current
                )

            else:

                current = 1

        latest_date = dates[-1]

        today = datetime.now().date()

        if (
            today - latest_date
        ).days > 1:

            current_streak = 0

        else:

            current_streak = 1

            for i in range(
                len(dates) - 1,
                0,
                -1
            ):

                difference = (
                    dates[i]
                    - dates[i - 1]
                ).days

                if difference == 1:

                    current_streak += 1

                else:

                    break

        return {
            "current_streak_days":
                current_streak,
            "longest_streak_days":
                longest
        }

    finally:

        db.close()
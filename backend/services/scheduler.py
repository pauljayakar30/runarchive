from apscheduler.schedulers.background import (
    BackgroundScheduler
)

scheduler = BackgroundScheduler()

scheduler.add_job(
    sync_activities,
    "cron",
    hour=6,
    minute=0
)

scheduler.start()
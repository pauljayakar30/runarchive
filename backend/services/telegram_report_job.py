from datetime import datetime

from backend.reports.monthly import (
    get_monthly_report
)

from backend.services.telegram_service import (
    send_telegram_message
)

from backend.services.report_formatter import (
    build_monthly_message
)


def monthly_report_job():

    now = datetime.now()

    report = get_monthly_report(
        now.year,
        now.month
    )

    message = build_monthly_message(
        report
    )

    send_telegram_message(
        message
    )
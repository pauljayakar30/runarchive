from backend.reports.monthly import (
    get_monthly_report
)

from backend.services.email_renderer import (
    render_monthly_email
)


def generate_monthly_html(
    year,
    month
):

    report = get_monthly_report(
    year,
    month
)

    html = render_monthly_email(
        report
    )

    return html
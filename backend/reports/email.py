from backend.reports.monthly import get_monthly_report
from backend.reports.insights import compare_months


def generate_monthly_email(
    year: int,
    month: int,
    previous_year: int,
    previous_month: int
):

    report = get_monthly_report(
        year,
        month
    )

    comparison = compare_months(
        year,
        month,
        previous_year,
        previous_month
    )

    improvement = comparison[
        "distance_change_percent"
    ]

    subject = (
        f"RunArchive - "
        f"{report['month']} Summary"
    )

    body = f"""
RunArchive Monthly Summary

Month: {report['month']}

Runs Completed: {report['total_runs']}
Distance: {report['total_distance_km']} km

Average Run: {report['average_run_km']} km
Longest Run: {report['longest_run_km']} km

Total Training Time:
{report['total_time_hours']} hours

Distance Change:
{improvement}% compared to last month

Keep showing up.
Progress compounds.
"""

    return {
        "subject": subject,
        "body": body.strip()
    }
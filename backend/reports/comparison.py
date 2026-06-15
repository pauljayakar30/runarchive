from backend.reports.monthly import get_monthly_report


def compare_months(
    current_year: int,
    current_month: int,
    previous_year: int,
    previous_month: int
):
    current = get_monthly_report(
        current_year,
        current_month
    )

    previous = get_monthly_report(
        previous_year,
        previous_month
    )

    current_distance = current.get(
        "total_distance_km",
        0
    )

    previous_distance = previous.get(
        "total_distance_km",
        0
    )

    if previous_distance == 0:
        improvement = None
    else:
        improvement = round(
            (
                (
                    current_distance
                    - previous_distance
                )
                / previous_distance
            ) * 100,
            2
        )

    return {
        "current_month": current,
        "previous_month": previous,
        "distance_change_percent": improvement
    }
def build_monthly_message(report):

    return f"""
🏃 RunArchive Monthly Summary

Month: {report['month']}

Runs: {report['total_runs']}
Distance: {report['total_distance_km']} km

Average Run: {report['average_run_km']} km
Longest Run: {report['longest_run_km']} km

Training Time: {report['total_time_hours']} hrs

Keep showing up.
Progress compounds.
"""
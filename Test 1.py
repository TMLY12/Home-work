from datetime import datetime
def get_days_from_today(date: str) -> int:
    try:
        today = datetime.today().date()
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (today-target_date).days
    except ValueError:
        print("Wrong format. Enter the date format: YYYY-MM-DD.")

from datetime import datetime

def validate_date(date_str):
    try:
        print(f"Input date string: {date_str}")
        # Parse the input date
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Parsed input_date: {input_date}")
        # Get today's date (without time for comparison)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        print(f"Today's date: {today}")
        # Check if the date is in the future or today
        is_future_or_today = input_date >= today  # Changed > to >=
        print(f"Is date in future or today? {is_future_or_today}")
        return is_future_or_today
    except ValueError as e:
        print(f"ValueError: {e}")
        # Invalid date format
        return False
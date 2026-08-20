# # =============================================================
# # datetime — dates, times, and arithmetic
# # =============================================================
# print("\n--- datetime module ---")
from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()

print(f"Today       : {today}")
print(f"Now         : {now}")
print(f"Formatted   : {now.strftime('%d/%m/%Y %H:%M:%S')}")

# # Date arithmetic using timedelta
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Tomorrow    : {tomorrow}")
print(f"Next week   : {next_week}")

# # Parse a string into a date object
date_str = "15-01-2024"
parsed_date = datetime.strptime(date_str, "%d-%m-%Y")
print(f"Parsed date : {parsed_date.date()}")

# # Days between two dates
join_date = date(2022, 6, 1)
days_served = (today - join_date).days
print(f"Days since joining 2022-06-01 : {days_served}")

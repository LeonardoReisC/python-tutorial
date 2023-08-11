# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
from pytz import timezone

# creating a date
date = datetime(2023, 7, 23, 18, 37, 00)
print(date)
print(date.year, date.month, date.day)
print('')

# using date formats
date_str = "2023-07-23 18:37:00"
date_format = "%Y-%m-%d %H:%M:%S"
date = datetime.strptime(date_str, date_format)
print(date)
print(date.strftime("%d/%m/%Y"))
print('')

# getting current time
date = datetime.now(timezone("America/New_York"))
print(date)
print('')

# using Unix TimeStamp
date = datetime.now()
timestamp = date.timestamp()
print(timestamp)
print(date.fromtimestamp(timestamp))  # current time
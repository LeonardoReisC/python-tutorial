from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y %H:%M:%S"
start = datetime.strptime("23/07/2023 18:37:00", fmt)
end = datetime.strptime("24/07/2023 10:45:30", fmt)

# timedelta
delta = timedelta(hours=16, minutes=8, seconds=30)
print(start + delta)
print('')

# relativedelta
rdelta = relativedelta(end, start)
print(rdelta)
print(end + relativedelta(seconds=59, minutes=10))
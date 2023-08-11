import calendar

print(calendar.calendar(2023, m=6))
print("----------------------------------------------------------------------"
      "----------------------------------------------------------------------"
      "-----------", "\n")
print(calendar.month(2023, 7))

print()

print(list(enumerate(calendar.day_name)))
first_day_number, last_day = calendar.monthrange(2023, 12)
print(first_day_number, last_day)

last_day_number = calendar.weekday(2023, 12, last_day)
print(last_day_number)
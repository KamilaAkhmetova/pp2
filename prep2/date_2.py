import datetime
d = datetime.date(2024, 3, 8) # year, month, day
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.isoweekday()) #monday is 1
print(tday.weekday()) # monday is 0

tdelta = datetime.timedelta(days = 7)
print(tday + tdelta) # may use + or -

bday = datetime.date(2025, 2, 15)
till_bday = bday - tday
print(till_bday) # or print(till_day.days)
print(till_bday.total_seconds())


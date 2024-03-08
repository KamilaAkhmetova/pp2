import datetime

dt = datetime.datetime(2005, 2, 15, 15, 2, 0, 0)# year, month, day, hours, minutes, sec, microsec
print(dt)
print(dt.date()) # or print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days = 7) # or hours = 12
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now() # timezone can be applied
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)



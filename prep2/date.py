import datetime

x = datetime.datetime.now()
print(x.year) # returns year

print(x.strftime("%A")) # returns day of the week
print(x.strftime("%a"))# short version of weekday
print(x.strftime("%w")) # weekday as number
print(x.strftime("%d")) # day of month
print(x.strftime("%B")) # returns a month

x = datetime.datetime(2020, 5, 17) # creates a year, month, day
print(x)
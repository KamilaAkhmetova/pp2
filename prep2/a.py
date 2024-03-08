import datetime
d = datetime.datetime.now()
tdelta = datetime.timedelta(days = 1) 
y = d - tdelta
t = d + tdelta
print(y.strftime('%d'))
print(d.strftime('%A'))
print(t.strftime('%A'))

dif = d - y
print(dif.total_seconds())
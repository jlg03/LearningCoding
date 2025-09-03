from datetime import datetime, date

today = date.today()
dat = datetime.strptime("2025-09-04", "%Y-%m-%d")
print(type(date))
print(type(dat))
print(dat.date() == today)
print(type(dat))
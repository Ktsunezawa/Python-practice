import datetime

today = datetime.date.today()
six = datetime.date(today.year, 6, 25)
delta = datetime.timedelta(days=60)

print(six + delta)

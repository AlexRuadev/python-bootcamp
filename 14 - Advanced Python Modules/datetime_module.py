import datetime

mytime = datetime.time(2, 20)

print(mytime)
print(mytime.hour)
print(mytime.minute)


today = datetime.date.today()
print(today)
print(today.year)

print(today.ctime())

from datetime import datetime
my_date_time = datetime(2021,3,18,21,58,1)
print(my_date_time)

# replace the year
my_date_time = my_date_time.replace(year = 2020)
print(my_date_time)

from datetime import date
date1 = date(2021,3,23)
date2 = date(1991,4,12)

result = date1 - date2
print(result)

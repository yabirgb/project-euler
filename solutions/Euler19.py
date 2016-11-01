#https://projecteuler.net/problem=19
import datetime
sundays = 0

for year in range(1901,2001):
    for month in range(1,13):
        if datetime.date(year,month,6).isoweekday() == 7:
            sundays += 1

print(sundays)

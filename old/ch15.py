import datetime

candidates = []
for year in range(2016,1582,-4):
	if datetime.date(year,1,1).weekday() == 3:
		if (year/1000) % 10 == 1 and year % 10 == 6:
			candidates.append(year)
candidates.append(1582)
print 'date: Jan 27,',candidates[len(candidates)-2]


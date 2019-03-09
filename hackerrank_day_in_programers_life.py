from datetime import datetime
from datetime import timedelta

if __name__ == '__main__' :
	intYear = int(input())
	days = 255

	if intYear < 1919 and intYear % 4 == 0 and intYear % 100 == 0:
		days = 254
	if intYear == 1918 :
		days = 268

	strDate = datetime.strftime(datetime(intYear,1,1) + timedelta(days=days), "%d.%m.%Y")
	print(strDate)
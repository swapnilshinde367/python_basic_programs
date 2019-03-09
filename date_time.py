from datetime import datetime
from datetime import timedelta

strDateTime = datetime(2016,1,1) + timedelta(days=255)

print( str(strDateTime.day) + '/' + str(strDateTime.month) + '/' + str(strDateTime.year) )
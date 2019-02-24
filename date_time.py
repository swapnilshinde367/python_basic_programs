from datetime import datetime
from datetime import timedelta

strDateTime = datetime.now() + timedelta(days=1)

print( str(strDateTime.day) + '/' + str(strDateTime.month) + '/' + str(strDateTime.year) )
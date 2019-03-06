from datetime import datetime

if __name__ == '__main__' :
	strTime = input()
	print( datetime.strftime( datetime.strptime( strTime, "%I:%M:%S%p" ), "%H:%M:%S" ) )
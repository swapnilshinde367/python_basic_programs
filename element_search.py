lstNumbers = [1, 2, 3, 4, 5, 6, 7, 9, 12, 19, 23, 24, 43, 45, 54, 78, 87, 98, 123, 234, 457, 654, 723, 856, 942, 967, 998]
inputnumber = int( input( 'Enter number : ' ) )

while( 1 ) :
	start = 0
	middle = len( lstNumbers ) // 2
	end = len( lstNumbers )

	if( 2 == len( lstNumbers ) ) :
		if( inputnumber in lstNumbers ) :
			print( 'Found it' )
		else :
			print( 'Nope not there' )
		# found = 1
		break
	if inputnumber > lstNumbers[middle] :
		lstNumbers = lstNumbers[middle:end]
		# print(lstNumbers)
	else :
		lstNumbers = lstNumbers[start:middle]
		# print(lstNumbers)

number = input( 'Gimmie number ' )
if False == number.isdigit() :
	print( 'You didn\'t give integer, bye!' )
else :
	number = int( number )
	if 0 == number % 2:
		print( 'It is even' )
	else :
		print( 'It is odd' )
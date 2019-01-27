intnumber = int( input( 'Enter number ' ) )

for i in range( 1, ( intnumber//2 ) + 1 ) :
	if( 0 == intnumber % i ) :
		print( i )
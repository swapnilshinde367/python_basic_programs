def generate_fibonacci() :
	a, b = 0, 1
	for i in range( 1, 10 ) :
		yield( a )
		a, b = b, a + b

for intNumber in generate_fibonacci() :
	print( intNumber )
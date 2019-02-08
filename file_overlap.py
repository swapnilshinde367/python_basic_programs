with open( 'primenumbers.txt', 'r' ) as prime_numbers_file :
	prime_numbers = (prime_numbers_file.readlines())

with open ( 'happynumbers.txt', 'r' ) as happy_numbers_file :
	happy_numbers = happy_numbers_file.readlines()

for i in prime_numbers :
	for j in happy_numbers :
		if( i == j ) :
			print( i.strip( '\n' ) )
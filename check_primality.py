import sys
number = input( 'Please enter number : ' )

if( False == number.isdigit() ):
	print( 'not a number' )
	sys.exit()
else :
		number = int(number)
		for i in range( 2, (number//2) + 1 ) :
			if( 0 == number% i ) :
				print( f'{number} is not prime' )
				sys.exit()
		print( f'{number} is prime' )

		#################################################### Print till n number #############################################################
		lstPrimes = []
		for i in range( 2, number + 1) :
			isPrime = 1
			for j in range( 2, (i//2)+1) :
				if( 0 == i % j ) :
					isPrime = 0
					break
			if( 1 == isPrime ) :
				lstPrimes.append( i )
		print(lstPrimes)

		#################################################### Print first n number of primes #############################################################

		lstPrimes = []
		i = 0
		rangedNumber = 2
		while( i < number ) :
			for j in range( 2, rangedNumber + 1 ) :
				isPrime = 1
				for k in range( 2, (rangedNumber // 2) + 1 ) :
					if( 0 == j % k ) :
						isPrime = 0
						break
			if( 1 == isPrime ) :
				lstPrimes.append( j )
				i = i + 1
			rangedNumber = rangedNumber + 1
		print( lstPrimes )



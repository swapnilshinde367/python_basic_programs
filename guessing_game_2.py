import sys
import random

print( 'Keep number in your head between 1 to 100, I will guess the nuber' )

guess_attempts = 1

start = 1
end = 100
middle = end // 2

while( 1 ) :

	middle = (start+end) // 2

	print( f'{start}, {middle}, {end}' )

	print( f'number is {middle}' )

	userinput = int( input( 'Press "1" for high, "2" for low, 3 for correct answer and 4 to quit : ' ) )
	if( 4 == userinput or 3 == userinput ) :
		print( f'Guesses = {guess_attempts}')
		sys.exit()
	elif( 1 == userinput ) :
		guess_attempts = guess_attempts + 1
		end = middle
	else :
		guess_attempts = guess_attempts + 1
		start = middle
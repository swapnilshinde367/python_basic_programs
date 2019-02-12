import sys
import random

tries = 0
secret_number = random.randint( 1, 9 )

while( 1 ) :
	user_input = input( 'Guess the number or press "q" to quit : ' )
	if( 'q' == user_input ) :
		print( f' Total tries : {tries} and correct number is {secret_number}')
		sys.exit()
	else :
		tries = tries + 1
		user_input = int( user_input )
		if( user_input == secret_number ) :
			print( 'There you are!' )
			print( f' Total tries : {tries}')
			sys.exit()
		elif( user_input < secret_number ) :
			print( 'Too low!' )
		else :
			print( 'To high!' )
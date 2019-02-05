import sys
import random

def cowsnbulls() :
	number = random.randint( 1000, 9999 )

	while(1) :
		userinput = input( 'Guess the number or press "q" to quit : ' )
		if 'q' == userinput :
			sys.exit()
		elif False == userinput.isdigit() or 4 != len( userinput ):
			print( 'Not a valid number, exiting' )
			sys.exit()
		else :
			cows = 0
			bulls = 0
			number = str(number)
			for i in range( len( userinput ) ):
				if( userinput[i] == number[i] ) :
					cows = cows + 1
				else :
					bulls = bulls + 1
			print( f'cows = {cows} and bulls = {bulls}' )
			if( 4 == cows ) :
				print( 'You got the 4 cows, number is correct' )
				sys.exit()

if __name__ == '__main__' :
	cowsnbulls()
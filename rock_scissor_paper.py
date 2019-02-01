quit_game = False
while False == quit_game :
	user_input = input( 'Enter "q" to quit the game or press enter to continue game ' )
	if "q" == user_input :
		print( 'Bye!' )
		quit_game = True
	else :
		player_1 = int( input( 'Player 1, enter your weapon no. \n 1. Rock \n 2. Scissor \n 3. Paper : ' ) )
		player_2 = int( input ( 'Player 2, enter your weapon no. \n 1. Rock \n 2. Scissor \n 3. Paper : ' ) )

		if( player_1 == player_2 ) :
			print( 'Tied!!' )
		elif( 1 == player_1 ) :
			print( player_1)
			print( player_2)
			if( 2 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
		elif( 2 == player_1 ) :
			if( 3 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
		elif( 3 == player_1 ) :
			if( 1 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
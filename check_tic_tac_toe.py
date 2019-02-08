lstGame = [[1, 2, 2],
	[2, 2, 0],
	[2, 1, 1]]

pl1 = 0
pl2 = 0
pln = 0

for i in range(len(lstGame)) :
	for j in range(len(lstGame)) :

		if( 0 == i and 0 == j ) :
			if( 1 == lstGame[i][j] ) :
				pl1 = 1
				pl2 = 0
				pln = 0
			elif( 2 == lstGame[i][j] ) :
				pl1 = 0
				pl2 = 1
				pln = 0
			else :
				pl1 = 0
				pl2 = 0
				pln = 1
		else :
			if( 1 == lstGame[i][j] and lstGame[i][j] == lstGame[i][j-1] and 1 == pl1 ) :
				pl1 = 1
				pl2 = 0
				pln = 0
			elif( 2 == lstGame[i][j] and lstGame[i][j] == lstGame[i][j-1] and 1 == pl2) :
				pl1 = 0
				pl2 = 1
				pln = 0
			else :
				pl1 = 0
				pl2 = 0
				pln = 1

		print ( lstGame[i][j],lstGame[i][j-1] )
	# print( '' )

	# print( '' )

# print( pl1, pl2, pln )
from itertools import groupby
strInput = input()

if strInput.isdigit() :
	for i,j in groupby(strInput) :
		print( '(' + str( len( list( j ) ) ) + ', ' + str(i) + ')', end = ' ' )
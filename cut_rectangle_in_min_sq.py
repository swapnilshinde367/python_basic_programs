# 36 - 2,3,4,6,9,12,18
# 30 - 2,3,5,6,10,15

def handleCalculateSquares( height, width ) :

	while height != width and 0 not in [height, width] :
		if height == width :
			print( '1 square of' + str(height) )
		elif height < width :
			print ( str(width // height) + ' squares of ' + str( height ) )
			height, width = width % height, height
		else :
			print (str(height // width) + ' squares of ' + str( width ))
			width, height = height % width, width

handleCalculateSquares( 30, 36 )
print('-'*10)
handleCalculateSquares( 13, 29 )
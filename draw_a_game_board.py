plot_range = int( input( 'Enter range : ' ) )
verticle = '|   '
horizontal = ' ---'

for i in range( plot_range ) :
	print( horizontal * plot_range )
	print( verticle * ( plot_range + 1 ) )
print( horizontal * plot_range )
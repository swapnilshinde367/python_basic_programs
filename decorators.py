def wrapping_item(func_name) :
	def wrapping_statemment() :
		return 'Wrapped your item {}'.format( func_name() )
	return wrapping_statemment

@wrapping_item
def new_bicycle() :
	return 'a bicycle'

print( new_bicycle() )

# One more example

def add_wrapping_style( style ) :
	def wrapping_item( func_name ) :
		def wrapping_statemment() :
			return 'A {} wrapped {} '.format( style, func_name() )
		return wrapping_statemment
	return wrapping_item

@add_wrapping_style( 'beautifully' )
def new_teddy() :
	return 'teddy!'

print( new_teddy() )
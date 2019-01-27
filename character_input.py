name = str( input( 'Please enter your name ' ) )
age = input( 'Please enter your age ' )
if( False == age.isdigit() ) :
	print( 'You didn\'t enter number' )
	print( 'Your name is ' + name )
else :
	print( 'Hi ' + name + ' you are still young and ' + age )
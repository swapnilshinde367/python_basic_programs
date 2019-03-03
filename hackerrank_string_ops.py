import re
if __name__ == '__main__':
	s = input()
	if( 0 != len(list(re.findall( '[0-9a-zA-Z]', s )) )):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[a-zA-Z]', s )) )) :
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[0-9]', s )) ) ):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[a-z]', s )) ) ):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[A-Z]', s )) ) ):
		print( True )
	else :
		print( False )
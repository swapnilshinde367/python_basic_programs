import re
with open( 'email_addresses.txt', 'r' ) as email_addresses :
	line = email_addresses.readline()
	while line :
		email_address = line.strip( '\n' )
		lstMatches = re.findall( "[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", email_address )
		if 0 != len(lstMatches) :
			print( lstMatches[0] )
		line = email_addresses.readline()
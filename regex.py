import re

strLine = "The rain in Spain"

# findall - prints all matches, returns "None" otherwise
lstMatches = re.findall( "ai", strLine )
print( lstMatches )

lstMatches = re.findall( "[\a-z]", strLine )
print( lstMatches )

# search - it searches for the match and if there are more than one match first one is returned returns "None" otherwise

lstMatches = re.search( 'rain', strLine )

print( lstMatches.start() )

# split - returns the list, where the string splits at match
lstMatches = re.split( 'ain', strLine )
print( lstMatches )

# sub - replaces every match with given string
lstMatches = re.sub( "\s", "9", strLine )
print( lstMatches )
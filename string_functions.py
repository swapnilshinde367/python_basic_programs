# Capitalize first letter of string
strLine = 'this is text'
print( strLine.capitalize() )

# title - Convert first character of the word to upper in given string
print( strLine.title )

# Upper - cinvert to uppercase
print( strLine.upper() )

# Lower - convert to lowercase
print( strLine.lower() )

# Casefold - convert to lowercase - simmilar to lower
print( strLine.casefold() )

# Swapcase - Swap the case of string
strLine = 'ThIs Is TeXt'
print( strLine.swapcase() )

# Count - Count the string occurances in given string
strLine ='I love apples, apple are my favorite fruit'
print( strLine.count( 'apple' ) )
print( strLine.count( 'e' ) )

#Startswith - returns true if it starts with given letter - This is case sensitive
print( strLine.startswith( 'i' ) )
print( strLine.startswith( 'I' ) )

#Endswith - returns true if it string ends with given character - Case sensitive function
print( strLine.endswith('t') )
print( strLine.endswith('T') )

# Find - finds the given string in string and returns position of first occurance else -1
print( strLine.find( 'apple' ) )

# Index - Returns the location of the searched string, in given string else raises exception
print( strLine.index( 'apple' ) )

#isalpha - Checks if the string has all letters
strLine = 'Test'
print( strLine.isalpha() )

# isalnum - check if the string is alphanumeric
strLine = 'Test123'
print( strLine.isalnum() )

# isdigit - Checks if string has all digits
strLine = '12345'
print( strLine.isdigit() )

# isdecimal - Checks if all characters are decimals
strLine = '12345'
print( strLine.isdecimal() )

# isnumeric - Checks if all characters are numeric
strLine = '1234567'
print( strLine.isnumeric() )

# islower - Checks if all character are lower
strLine = 'test'
print( strLine.islower() )

# isupper - Checks if all characters are upper
strLine = 'TEST'
print( strLine.isupper() )

# join - joins the list items by a seperator
lstNames = ['one', 'two', 'three', 'four']
print( ' & '.join( lstNames ) )

# split - Split the string by seperator and converts it to list
strLine = '&'.join( lstNames )
print( strLine.split( '&' ) )

# replace - replace the substrings by given string
strLine ='I love apples, apples are my favorite fruit'
strLine = strLine.replace( 'apples', 'mangoes' )
print( strLine )

# lstrip - strip spaces/characters from left of the string
strLine ='        Banana             Apple'
print( strLine.lstrip() )

# rstrip - strip spaces/characters from right of the string
strLine ='Apple        Banana             '
print( strLine.rstrip() )

# rfind - find last occurance of substring in a given string
strLine ='I love apples, apples are my favorite fruit'
print( strLine.rfind( 'apple' ) )

# rsplit - will start splitting from right and max is the number how many parts to b
# e split into, if not given it works as split()
strLine ='I love apples, apples are my favorite fruit'
print( strLine.rsplit( ' ', 2 ) )

# splitline - Split the string where new line is given
strLine = "Thank you for the music\nWelcome to the jungle"
print(strLine.splitlines())


# zfill - insert the zeros at begining of the string till it reaches the length
strLine = 'Zero'
print( strLine.zfill( 10 ) )
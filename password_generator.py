import random
import string

password = ''
password = password + ''.join( random.sample( string.ascii_lowercase, 5) )
password = password + ''.join( random.sample( string.ascii_uppercase, 5 ) )
password = password + ''.join( random.sample( string.digits, 6 ) )
password = password + ''.join( random.sample( string.punctuation, 4 ) )

password = list( password )
random.shuffle( password )

print( ''.join( password ) )

print(string.digits)
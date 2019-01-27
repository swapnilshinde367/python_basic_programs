from random import randint

lstintRandom1 = range( 0, randint( 1, 100 ) )
lstintRandom2 = range( 0, randint( 1, 100 ) )

print( lstintRandom1 )
print( lstintRandom2 )

print( [ i for i in lstintRandom1 if i in lstintRandom2 ] )
import random

listA = random.sample( range( 100 ), 15 )
listB = random.sample (range( 100 ), 20 )

print(listA)
print(listB)

print( [ i for i in set(listA) if i in set(listB)] )
from itertools import product

if __name__ == '__main__' :
	list1 = map( int, input().split() )
	list2 = map( int, input().split() )

	for i in product(list1, list2) :
		print( i, end = ' ' )
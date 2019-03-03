from itertools import groupby

def sockMerchant(n, ar):
	ar = groupby( ar )
	totalSocks = 0
	for i,j in ar :
		totalSocks = totalSocks + len( list( j ) ) // 2
	return totalSocks

if __name__ == '__main__':
	n = int(input())
	ar = list(map(int, input().rstrip().split()))
	ar.sort()
	totalSocks = sockMerchant(n, ar)

	print( totalSocks )
from itertools import groupby

if __name__ == '__main__' :
	n = int(input())
	totalCandles = list(map(int,input().rstrip().split()))
	totalCandles.sort(reverse = True )
	totalCandles = groupby(totalCandles)
	print(totalCandles)
	for i,j in totalCandles :
		print(len(list(j)))
		break
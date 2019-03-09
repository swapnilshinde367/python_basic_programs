#!/bin/python3
# Complete the plusMinus function below.
def plusMinus(arr):

	intTotalPositive = 0
	intTotalNegative = 0
	intTotalZeros = 0

	for i in arr:
		if i < 0 :
			intTotalNegative = intTotalNegative + 1
		elif i > 0 :
			intTotalPositive = intTotalPositive + 1
		else :
			intTotalZeros = intTotalZeros + 1

	print( "{0:.6f}".format(round(intTotalPositive/len(arr),6)) )
	print("{0:.6f}".format(round(intTotalNegative/len(arr),6)))
	print( "{0:.6f}".format(round(intTotalZeros/len(arr),6)) )

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	plusMinus(arr)
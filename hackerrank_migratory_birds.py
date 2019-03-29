from itertools import groupby

def migratoryBirds(arr):
	arr.sort()
	intCount = 0
	for i, j in groupby(arr) :
		inTotalCount = len(list(j))
		if intCount < inTotalCount :
			intCount = inTotalCount
			intNumber = i
	print(intNumber)

if __name__ == '__main__':
	arr_count = int(input().strip())
	arr = list(map(int, input().rstrip().split()))
	result = migratoryBirds(arr)

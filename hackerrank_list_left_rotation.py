def rotLeft( oldList, intRotations ):
	newList = oldList.copy()
	intListLength = len(oldList)
	intShiftPosition = len(oldList) - intRotations
	i = 0
	while i < intRotations :
		newList[i+intShiftPosition] = oldList[i]
		i = i + 1
	i = 0
	while i < intShiftPosition :
		newList[i] = oldList[intRotations+i]
		i = i + 1
	return newList

if __name__ == '__main__':

	nd = input().split()

	n = int(nd[0])

	d = int(nd[1])

	a = list(map(int, input().rstrip().split()))

	result = rotLeft(a, d)
	print( ' '.join( str(i) for i in result ) )
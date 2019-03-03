if __name__ == '__main__' :
	n = int(input())
	lstNumbers = list(map(int,input().split()))
	intPosition = 0
	intJumpCount = 0

	while intPosition < len(lstNumbers)-2 :
	# for intPosition in range(0,len(lstNumbers)-2) :
		# print(intPosition)
		# if 1 != lstNumbers[intPosition] :
		if 0 == lstNumbers[intPosition] and 0 == lstNumbers[intPosition+2] :
			# print( '--1--', end = ' ')
			# print(intPosition)
			intPosition = intPosition + 2
			intJumpCount = intJumpCount + 1
		elif 0 == lstNumbers[intPosition] and 0 == lstNumbers[intPosition+1] and 1 == lstNumbers[intPosition+2] :
			# print( '--2--', end = ' ')
			# print(intPosition)
			intPosition = intPosition + 1
			intJumpCount = intJumpCount + 1
		else :
			intPosition = intPosition + 1

	if 0 == lstNumbers[len(lstNumbers)-2] :
		intJumpCount = intJumpCount + 1

	print(intJumpCount)
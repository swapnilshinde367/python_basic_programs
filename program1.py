from itertools import groupby
def findDifferentWays(size, allowedChanges, str):

	lstNumbers = list(map(int, list(str) ))

	lstNumbers.sort()

	lstLengths = []
	for i,j in groupby(lstNumbers) :
		lstLengths.append( len(list(j)) )

	# print(lstLengths)
	numofZeros = lstLengths[0]
	numofOnes = lstLengths[1]

	if allowedChanges < numofZeros :
		return (numofOnes - allowedChanges)
	elif allowedChanges == numofZeros :
		return numofZeros-numofOnes
	else :
		return allowedChanges


print(findDifferentWays(7,1,'1010101'))
print(findDifferentWays(5,3,'01010'))
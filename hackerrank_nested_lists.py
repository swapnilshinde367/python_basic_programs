from itertools import groupby
from operator import itemgetter

if __name__ == '__main__':

	lstStudentGrades= []

	for _ in range(int(input())):
		name = input()
		score = float(input())
		lstStudentGrades.append([name,score])

	lstStudentGrades.sort( key = lambda x : x[1] )
	y = groupby(lstStudentGrades, lambda x: x[1])

	intCount = 1
	for i,j in y:
		if 2 == intCount :
			lstNames = [x[0] for x in list(j)]
			lstNames.sort()
			for strName in lstNames :
				print( strName )
		intCount = intCount + 1
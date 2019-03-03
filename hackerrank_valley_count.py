from itertools import groupby
if __name__ == '__main__':
	n = int(input())
	lstSteps = list(input())
	valleycount = 0
	previous = ''
	for i,j in groupby(lstSteps) :
		if 'D' == previous and 'U' == i and 1 < len(list(j)) :
			valleycount = valleycount + 1
		previous = i
	print(valleycount)

# This script has failed exam.
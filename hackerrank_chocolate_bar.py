def birthday(s, d, m):

	intTotalWays = 0
	# print( len(s) - m)
	for i in range( len(s) ):
		# print(i)
		nextValSum = 0
		for j in range(m) :
			if i+j < len(s) :
				nextValSum = nextValSum + s[i+j]
		if nextValSum == d :
			intTotalWays = intTotalWays + 1

	return intTotalWays

if __name__ == '__main__':
	n = int(input().strip())
	s = list(map(int, input().rstrip().split()))
	dm = input().rstrip().split()
	d = int(dm[0])
	m = int(dm[1])
	result = birthday(s, d, m)
	print(result)
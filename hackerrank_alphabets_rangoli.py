import string

def print_rangoli(size):
	lstAlphabets = list(string.ascii_lowercase)[:size]
	lstAlphabets.reverse()
	lstPattern = []
	i = (size*2) - 2
	j = 0
	while i >= 0 :
		lstMiddlePattern = []
		strPattern = '-' * (i)
		# print(strPattern, end='')
		for k in range(0,j+1) :
			lstMiddlePattern.append( lstAlphabets[k] )
		l = j - 1
		while l >= 0 :
			lstMiddlePattern.append( lstAlphabets[l] )
			l = l - 1
		strPattern = strPattern + '-'.join( lstMiddlePattern )
		strPattern = strPattern + '-' * (i)
		i = i - 2
		j = j + 1
		print(strPattern)
		lstPattern.append(strPattern)
	lstPattern.pop()
	for i in lstPattern[::-1] :
		print(i)
if __name__ == '__main__':
	n = int(input())
	print_rangoli(n)
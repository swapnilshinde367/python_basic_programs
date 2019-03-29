if __name__ == '__main__' :
	mn = list(map(int,input().strip().split()))
	m = mn[0]
	n = mn[1]
	j = 2
	strlstLines = []
	for i in range( 1, m, 2 ):
		dashes = ( n - ( i*3 ) ) // 2
		strLine = '-' * dashes
		strLine = strLine + '.|.' * i
		strLine = strLine + '-' * dashes
		print(strLine)
		strlstLines.append(strLine)
	print( '-' * ( ( n - 7 ) // 2 ) + 'WELCOME' + '-' * ( ( n - 7 ) // 2 ) )
	strlstLines.reverse()
	for i in strlstLines :
		print(i)
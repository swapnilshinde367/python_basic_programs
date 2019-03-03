if __name__ == '__main__':
	lstOperations = ['insert','remove','append','sort','pop','reverse','print']
	lstNumbers = []
	n = int(input())
	for _ in range(n) :
		strOperation, *lstOpNumbers = input().split()
		lstOpNumbers = list(map(int,lstOpNumbers))
		if( strOperation in lstOperations ) :
			if( 'insert' == strOperation ) :
				lstNumbers.insert( lstOpNumbers[0], lstOpNumbers[1] )
			elif( 'remove' == strOperation ) :
				lstNumbers.remove(lstOpNumbers[0])
			elif( 'append' == strOperation ) :
				lstNumbers.append(lstOpNumbers[0])
			elif( 'sort' == strOperation ) :
				lstNumbers.sort()
			elif( 'pop' == strOperation ) :
				lstNumbers.pop()
			elif( 'reverse' == strOperation ) :
				lstNumbers.reverse()
			else :
				print( lstNumbers )
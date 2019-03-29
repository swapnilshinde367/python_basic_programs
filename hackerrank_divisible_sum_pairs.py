if __name__ == '__main__' :
	nk = list(map(int, input().strip().split()))
	intDivisor = nk[1]
	lstNumbers = list(map(int, input().strip().split()))

	print( ([(i,j) for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0]) )
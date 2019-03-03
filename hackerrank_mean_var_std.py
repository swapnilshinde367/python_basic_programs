import numpy as np

if __name__ == '__main__' :
	lstNumbers=[]
	n, m = map(int,input().split())
	for _ in range( n ) :
			lstNumbers.append(list(map(int,input().split())))
	lstNumbers = np.array(lstNumbers)
	print( np.mean(lstNumbers, axis = 1 ) )
	print( np.var(lstNumbers, axis = 0 ) )
	print( np.std(lstNumbers, axis = None ) )
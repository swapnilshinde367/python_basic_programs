# f = lambda x,y : return x + y

f = lambda x : x*x
lstNumbers = [1,2,3,4,5]

print( [f(i) for i in lstNumbers] )

x = map( f, lstNumbers )

print(list(x))


def filtereven( i ):
	if 0 == i % 2 :
		return True
	return False

x = filter( filtereven, lstNumbers)
print(list(x))

def filterodd() :
	lstNumbers = [1,2,3,4,5]
	for i in lstNumbers :
		if 1 == i % 2 :
			yield i

x = filterodd()
for i in x:
	print( i )
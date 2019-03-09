import sys
def kangaroo(x1, v1, x2, v2):

	for i in range(10000) :
		if x1 == x2 :
			print('YES')
			sys.exit()
		x1 = x1 + v1
		x2 = x2 + v2

	print('NO')


if __name__ == '__main__':

	arrNumbers = list(map(int, input().strip().split()))
	x1 = arrNumbers[0]
	v1 = arrNumbers[1]
	x2 = arrNumbers[2]
	v2 = arrNumbers[3]
	if x1 < x2 and v1 < v2 :
		print('NO')
	else :
		result = kangaroo(x1, v1, x2, v2)
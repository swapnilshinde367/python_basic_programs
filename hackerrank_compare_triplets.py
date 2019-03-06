# Complete the compareTriplets function below.
def compareTriplets(a, b):
	ascore = 0
	bscore = 0
	for i in range(len(a)) :
		if a[i] > b[i] :
			ascore = ascore + 1
		elif a[i] < b[i] :
			bscore = bscore + 1
	return f'{ascore} {bscore}'

if __name__ == '__main__':
	a = list(map(int, input().rstrip().split()))

	b = list(map(int, input().rstrip().split()))

	result = compareTriplets(a, b)
	print(result)
import string
def solve(s):
	return string.capwords(s, ' ')
	# lst = []
	# for i in s.split() :
	# 	print(i)
	# 	lst.append( i.capitalize() )
	# return ' '.join( lst )

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	print(solve(s))

	# fptr.write(result + '\n')

	# fptr.close()
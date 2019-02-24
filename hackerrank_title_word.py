def solve(s):

	lst = []
	if 0 < len( s ) and len( s ) < 1000 :
		for i in s.split() :
			lst.append( i.capitalize() )
	return ' '.join( lst )

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	print(solve(s))

	# fptr.write(result + '\n')

	# fptr.close()
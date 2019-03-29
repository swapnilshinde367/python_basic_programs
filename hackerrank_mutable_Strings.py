def mutate_string( strInput, intIndex, strChar):
	strInput = list(strInput)
	strInput[intIndex] = strChar
	return ''.join(strInput)


if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)
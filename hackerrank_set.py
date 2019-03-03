if __name__ == '__main__' :
	s = set()
	n = int(input())
	for _ in range(n) :
		strCountry = input()
		s.add(strCountry)
	print(len(s))
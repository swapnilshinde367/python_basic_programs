if __name__ == '__main__':
	s = input()
	n = int(input())

	intTotalCountOfFirstChar = s.count("a")
	intTotalOccurances = ( n // len(s) * intTotalCountOfFirstChar )
	intTotalOccurances = intTotalOccurances + s[:n%len(s)].count("a")
	print(intTotalOccurances)
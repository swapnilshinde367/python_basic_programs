def count_substring(strParent, strSubString):
	i = 0
	totalMatches = 0
	while i < len(strParent) :
		intPosition = strParent.find(strSubString)
		if -1 != intPosition :
			totalMatches = totalMatches + 1
			strParent = strParent[intPosition+1:]
		else :
			break

	return totalMatches

if __name__ == '__main__' :
	strParent = input().strip()
	strSubString = input().strip()
	count = count_substring(strParent, strSubString)
	print(count)

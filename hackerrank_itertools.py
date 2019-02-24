from itertools import combinations_with_replacement
strWord = input()
strWord = strWord.split()
intNumber = int(strWord[1])
strWord = list(strWord[0])

if True == ''.join(strWord).isupper() and 0 < intNumber and intNumber <= len(strWord) :
	strWord.sort()
	for i in combinations_with_replacement( strWord, intNumber ) :
		print(''.join(i))
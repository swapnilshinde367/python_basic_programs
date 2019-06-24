n = int(input('enter number : '))

for i in range(n) :

	strUid = input('enter string : ')

	lstUid = set(list(strUid))
	intCount = 0
	strUpCount = 0

	if strUid.isalnum() and 10 == len(lstUid):
		for inputchar in strUid :
			if inputchar.isdigit() :
				intCount = intCount + 1
			if inputchar.isupper() :
				strUpCount = strUpCount + 1

	if 2 <= strUpCount and 3 <= intCount :
		print( 'Valid' )
	else :
		print( 'Invalid' )
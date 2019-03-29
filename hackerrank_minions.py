def minion_game(string):
	string = string.lower()
	kevin = 0
	stuart = 0
	for i in range(len(string)) :
		if string[i] in ['a','e','i','o','u'] :
			# kevin = kevin + len(string[i:])
			kevin = kevin + (len(string)-i)
		else :
			# stuart = stuart + len(string[i:])
			stuart = stuart + (len(string)-i)

	if kevin > stuart :
		print( f"Kevin {kevin}" )
	elif kevin < stuart :
		print( f"Stuart {stuart}" )
	else :
		print( 'Draw' )

if __name__ == '__main__':
	s = input().lower()
	minion_game(s)
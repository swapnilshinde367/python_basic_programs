with open( 'writetofile.txt', 'w' ) as open_file:
	for i in range(10) :
		open_file.writelines( str(i) )
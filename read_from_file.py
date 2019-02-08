names = {}
with open( 'names.txt', 'r' ) as open_file :
	line = open_file.readline()
	while line :
		line = line.strip( '\n' )
		if line not in names :
			# names.append( line )
			names[line] = 1
		else :
			names[line] = names[line] + 1
		# print(line)
		line = open_file.readline()
print(names)
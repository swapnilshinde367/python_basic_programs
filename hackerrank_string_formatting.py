if __name__ == '__main__' :
	n = int(input())
	width = len(bin(n)[2:])
	for i in range( 1, n + 1 ) :
		print( str(i).rjust(width, ' '), end = ' ' )
		print(oct(i)[2:].rjust(width, ' '), end = ' ' )
		print(str(hex(i)).upper()[2:].rjust(width, ' '), end = ' ' )
		print(bin(i)[2:].rjust(width, ' '))
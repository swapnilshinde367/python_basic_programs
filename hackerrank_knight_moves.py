x = 3
y = 3

for i in range(8) :
	for j in range(8) :
		if (x-i in [2,-2] and y-j in [1,-1]) or (x-i in [1,-1] and y-j in [2,-2]) :
			print(i,j)
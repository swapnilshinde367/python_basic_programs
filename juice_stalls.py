import sys
numOfStalls, distOfStalls, juiceQuantity, distance, initialEnergy = input().split(',')

distCoverd = 0
while( distCoverd <= distance ) :
	distCoverd = distCoverd + initialEnergy
	for i in range(len(distOfStalls)) :
		if(distOfStalls[i] > initialEnergy )
			print(-1)
			sys.exit()
		else:
			if( initialEnergy <= (distOfStalls[i+1] - distOfStalls[i])) :
				initialEnergy = initialEnergy - distOfStalls[i] + juiceQuantity[i]
			else :
				continue
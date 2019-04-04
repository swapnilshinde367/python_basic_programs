import sys

numOfStalls = 4
distOfStalls =  [5,7,8,10]
juiceQuantity = [2,5,2,6]
distance = 15
initialEnergy = 17

numOfStalls = int(raw_input())
distOfStalls =  map( int, (raw_input()).split() )
juiceQuantity = map( int, (raw_input()).split() )
distance = int(raw_input())
initialEnergy = int(raw_input())


# initialEnergy = 5
# juiceQuantity = [2,3,1,5]

stallsVisited = 0
disttocover = 0
currentEnergy = initialEnergy

if initialEnergy >= distance :
	print(0)
	sys.exit()

i = 0
while i < numOfStalls :

	if( i == 0 ) :
		disttocover = distOfStalls[i]
	else :
		disttocover =  distOfStalls[i] - distOfStalls[i-1]

	juiceAtStall = juiceQuantity[i]

	currentEnergy = currentEnergy - disttocover

	if currentEnergy > 0 :
		j = i + 1
		while j < numOfStalls :

			disttocover1 =  distOfStalls[j] - distOfStalls[j-1]

			if currentEnergy - disttocover1 > 0 :
				currentEnergy = currentEnergy - disttocover1
				j = j + 1
				i = j - 1
			elif (currentEnergy - disttocover1) == 0:
				currentEnergy = (currentEnergy - disttocover1) + juiceQuantity[j]
				j = j + 1
				i = j
				stallsVisited = stallsVisited + 1
				break
			else :
				print(-1)
				sys.exit()

	elif currentEnergy == 0 :
		stallsVisited = stallsVisited + 1
		currentEnergy = currentEnergy + juiceAtStall
		i = i + 1
	else :
		print(-1)
		sys.exit()

if( currentEnergy < (distance - distOfStalls[numOfStalls-1]) ) :
	print(-1)
else :
	print(stallsVisited)


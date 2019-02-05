number = input( 'Enter number : ' )
if False == number.isdigit() :
	print( 'not a number' )
else :
	number = int( number )
	################### Print first n fibonacci numbers ##############################
	lstFibbo = []
	a = 1
	b = 1
	for i in range(number) :
		lstFibbo.append(a)
		a , b = b, a + b
	print(lstFibbo)
	################### Print all fibonacci numbers less than n ##############################
	lstFibbo = []
	a = 1
	b = 1
	while a < number :
		lstFibbo.append(a)
		a,b = b, a+b
	print( lstFibbo )
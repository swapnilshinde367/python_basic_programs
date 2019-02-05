lstNumbers = [1,2,3,4,5,6,7,9,9,987,4,234,5,3456,2,1,234,6,2,112,34,56,2,2345,2,345,6,2,334,43,123,4,45,3]

print(len((lstNumbers)))
print((list(set(lstNumbers))))

lstNew = []
for i in lstNumbers :
	if( i not in lstNew ):
		lstNew.append(i)

print(lstNew)
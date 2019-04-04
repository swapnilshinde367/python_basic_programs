numbers = map( int, (raw_input()).split() )
start, rows, columns = numbers[0], numbers[1], numbers[2]

x = []
for i in range(0,rows) :
	rows = []
	for j in range(0,columns) :
		rows.append(start)
		start = start +1
	x.append(rows)

print(x)


result = x

xt =x

xt = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
print(xt)

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*xt)] for X_row in x]

for r in result:
	print(r)
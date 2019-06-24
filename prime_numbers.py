lst = [1,2,3,4,5,6]

z = map( lambda x : x*x, lst)

print(list(z))

z = filter( lambda x : x+2, lst )

print(list(z))
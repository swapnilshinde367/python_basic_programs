######### Decorator
def wrapping_item(func_name) :
	def wrapping_statement() :
		return 'A nicely wrapped ' + func_name()
	return wrapping_statement

@wrapping_item
def wrap_item() :
	return 'teddy'

print(wrap_item())


####### Class Inheritance
class CPerson() :

	def __init__(self, name) :
		self.name = name

	def intro(self) :
		print( 'My name is ' + self.name, end = ' ' )

class CSuperHero( CPerson ) :

	def __init__( self, name, superName ) :
		super( CSuperHero, self ).__init__( name )
		self.superName = superName

	def intro( self ) :
		super( CSuperHero, self ).intro()
		print( 'and I am ' + self.superName )

objSuperHero = CSuperHero('Wade', 'Deadpool')

objSuperHero.intro()

######### Context Manager
class TestManager() :

	def __init__(self) :
		print('Initiated')

	def __enter__(self) :
		print('Entered in context')

	def __exit__( self, exc_type, exc_value, exc_traceback ) :
		print('Finished')

with TestManager() as manager :
	print('Executing')

######## Class Method, Static Method, Property
class Cperson() :
	salary_perc = 1.50

	def __init__(self, fname, lname) :
		self.fname = fname
		self.lname = lname
	@property
	def full_name(self):
		return self.fname + ' ' + self.lname

	@full_name.setter
	def full_name(self, full_name) :
		self.fname = full_name.split()[0]
		self.lname = full_name.split()[1]

	@classmethod
	def set_salary_perc(cls, perc) :
		cls.salary_perc = perc

	@staticmethod
	def print_hello() :
		print('hello')

objPerson = Cperson('John', 'Smith')
print(objPerson.full_name)
Cperson.set_salary_perc(2.0)
print(objPerson.salary_perc)
Cperson.print_hello()

####### Anagram
s1 = 'tabs'
s2 = 'bats'
print(sorted(s1) == sorted(s2))


#### Min Dist

s = "the quick the brown quick brown the frog"
w1 = "quick"
w2 = "frog"
words = s.split()
if w1 == w2 :
	print(0)
minDist = len(words)
for start in range(len(words)) :
	if w1 == words[start] :
		for end in range(len(words)) :
			if w2 == words[end] :
				if minDist > end-start-1 :
					minDist = end-start-1
print(minDist)

###### All alphabets from a-z
strInput = 'The quick brown fox jumps over the lazy dog'
strInput = set(strInput)
lstChars = [ ch for ch in strInput if ord(ch) in range(ord('a'), ord('z')+1) ]
if len(lstChars) == 26 :
	print(True)

###### Prime number till range
number = 10
rangedum = 2
lstPrimes = []
i = 0
while i < number :
	for j in range(2, rangedum+1) :
		isPrime = 1
		for k in range(2,j//2+1) :
			if j%k == 0 :
				isPrime = 0
				break
	if isPrime == 1 :
		lstPrimes.append(j)
		i = i+ 1
	rangedum = rangedum + 1
print(lstPrimes)

#### Fibonacci
a=1
b=1
for i in range(number) :
	print(a, end=',')
	a,b = b, a+b
a = 1
b = 1
while a < number :
	print(a, end=',')
	a,b = b, a+b

######## Chess Knight
x = 2
y = 0

for i in range(8) :
	for j in range(8) :
		if (x-i in [2,-2] and y-j in [1,-1]) or (x-i in [1,-1] and y-j in [2,-2]) :
			print(i,j)

###### Reverse String
strName = 'My name is Michael'
print(' '.join(strName.split()[::-1]))


######### Cut Reactangle
height = 30
width = 36

while height != width and 0 not in [height,width] :
	if height == width :
		print( f'1 sq of {height}' )
	elif height < width :
		print( f'{width//height} sq of {height}' )
		height, width = width % height , height
	else :
		print( f'{height//width} sq of {width}' )
		width, height = height%width, width

######### Email Addresses - Regex
import re
with open("email_addresses.txt", 'r') as email_file :
	line = email_file.readline()
	while line :
		lstMatches = re.findall( '[a-zA-Z0-9]+@[a-zA-z0-9]+\.[a-zA-Z0-9]+', line )
		if 0 < len(lstMatches) :
			print(lstMatches[0])
		line = email_file.readline()

####### IP - regex
strip = '127.0.0.1'

lstMatches = re.findall( r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', strip )
if 0 < len(lstMatches) :
	print('Valid')
else :
	print('Invalid')

def wrapping_item(func_name) :
	def wrapping_statement() :
		return 'A beautifully wrapped ' + func_name()
	return wrapping_statement

@wrapping_item
def wrap_item() :
	return 'teddy.'

print(wrap_item())


class ContextManager() :

	def __init__(self) :
		print('init')

	def __enter__(self):
		print('enter method called')
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback) :
		print('exited')

with ContextManager() as manager :
	print('statement')


class CPerson() :
	salary = 1000
	def __init__(self, name) :
		self.name = name

	def intro(self) :
		print('My name is ' + self.name)

	@classmethod
	def update_salary( cls, salary ) :
		cls.salary = salary

	@staticmethod
	def say_hello() :
		print('hello')

obj = CPerson('ABC')
print(obj.salary)
obj.update_salary(1500)
print(obj.salary)
CPerson.update_salary(2000)
print(obj.salary)
CPerson.say_hello()

class CSuperhero( CPerson ) :
	def __init__(self, name, supername) :
		super(CSuperhero, self).__init__(name)
		self.supername = supername

	def intro(self) :
		super(CSuperhero, self).intro()
		print( 'and I am ' + self.supername )

	@property
	def both_names(self):
		return self.supername + ' is ' + self.name

	@both_names.setter
	def both_names(self,names):
		self.name, self.supername = names.split( ' ')[0], names.split( ' ' )[1]


obj = CSuperhero('Wade', 'Deadpool')
obj.intro()
print(obj.both_names)
obj.both_names = "Peter Spiderman"
print(obj.both_names)
obj.intro()

#anagram
str1 = 'listen'
str2 = 'silent'
print( sorted(str1) == sorted(str2) )

#min distance

s = "the quick the brown quick brown the frog"
w1 = "frog"
w2 = "quick"
if w1 == w2 :
	print(0)
words = s.split()
minDist = len(words) + 1
for start in range(len(words)) :
	if w1 == words[start] :
		for end in range(len(words)) :
			if w2 == words[end] :
				if minDist > end-start-1 :
					minDist = end-start-1
print(minDist)


strInput = 'The quick brown fox jumps over the lazy dog'

strInput = set(strInput.lower())

alphas = [ ch for ch in strInput if ord(ch) in range(ord('a'),(ord('z')+1))]

if 26 == len(alphas):
	print(True)
else :
	print(False)


import re

strPass = 'abcDFE123@#$'

if 5 < len(strPass) :
	print( re.findall( '([a-z])([A-Z])([0-9])', strPass ) )


lstPrimes = []
i = 0
number = 10
rangednum = 2
while i < number :
	for j in range(2,rangednum+1) :
		isPrime = 1
		for k in range(2,j//2) :
			if j%k == 0 :
				isPrime = 0
				break
	if isPrime == 1 :
		lstPrimes.append(j)
		i = i + 1
	rangednum = rangednum + 1
print(lstPrimes)
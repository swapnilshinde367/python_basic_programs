
##########
#character_input.py
##########
name = str( input( 'Please enter your name ' ) )
age = input( 'Please enter your age ' )
if( False == age.isdigit() ) :
	print( 'You didn\'t enter number' )
	print( 'Your name is ' + name )
else :
	print( 'Hi ' + name + ' you are still young and ' + age )
##########
#check_email_addresses_from_file.py
##########
import re
with open( 'email_addresses.txt', 'r' ) as email_addresses :
	line = email_addresses.readline()
	while line :
		email_address = line.strip( '\n' )
		lstMatches = re.findall( "[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", email_address )
		if 0 != len(lstMatches) :
			print( lstMatches[0] )
		line = email_addresses.readline()
##########
#check_primality.py
##########
import sys
number = input( 'Please enter number : ' )

if( False == number.isdigit() ):
	print( 'not a number' )
	sys.exit()
else :
		number = int(number)
		for i in range( 2, (number//2) + 1 ) :
			if( 0 == number% i ) :
				print( f'{number} is not prime' )
				sys.exit()
		print( f'{number} is prime' )

		#################################################### Print till n number #############################################################
		lstPrimes = []
		for i in range( 2, number + 1) :
			isPrime = 1
			for j in range( 2, (i//2)+1) :
				if( 0 == i % j ) :
					isPrime = 0
					break
			if( 1 == isPrime ) :
				lstPrimes.append( i )
		print(lstPrimes)

		#################################################### Print first n number of primes #############################################################

		lstPrimes = []
		i = 0
		rangedNumber = 2
		while( i < number ) :
			for j in range( 2, rangedNumber + 1 ) :
				isPrime = 1
				for k in range( 2, (rangedNumber // 2) + 1 ) :
					if( 0 == j % k ) :
						isPrime = 0
						break
			if( 1 == isPrime ) :
				lstPrimes.append( j )
				i = i + 1
			rangedNumber = rangedNumber + 1
		print( lstPrimes )



##########
#check_tic_tac_toe.py
##########
lstGame = [[1, 2, 2],
	[2, 2, 0],
	[2, 1, 1]]

pl1 = 0
pl2 = 0
pln = 0

for i in range(len(lstGame)) :
	for j in range(len(lstGame)) :

		if( 0 == i and 0 == j ) :
			if( 1 == lstGame[i][j] ) :
				pl1 = 1
				pl2 = 0
				pln = 0
			elif( 2 == lstGame[i][j] ) :
				pl1 = 0
				pl2 = 1
				pln = 0
			else :
				pl1 = 0
				pl2 = 0
				pln = 1
		else :
			if( 1 == lstGame[i][j] and lstGame[i][j] == lstGame[i][j-1] and 1 == pl1 ) :
				pl1 = 1
				pl2 = 0
				pln = 0
			elif( 2 == lstGame[i][j] and lstGame[i][j] == lstGame[i][j-1] and 1 == pl2) :
				pl1 = 0
				pl2 = 1
				pln = 0
			else :
				pl1 = 0
				pl2 = 0
				pln = 1

		print ( lstGame[i][j],lstGame[i][j-1] )
	# print( '' )

	# print( '' )

# print( pl1, pl2, pln )
##########
#cows_and_bulls.py
##########
import sys
import random

def cowsnbulls() :
	number = random.randint( 1000, 9999 )

	while(1) :
		userinput = input( 'Guess the number or press "q" to quit : ' )
		if 'q' == userinput :
			sys.exit()
		elif False == userinput.isdigit() or 4 != len( userinput ):
			print( 'Not a valid number, exiting' )
			sys.exit()
		else :
			cows = 0
			bulls = 0
			number = str(number)
			for i in range( len( userinput ) ):
				if( userinput[i] == number[i] ) :
					cows = cows + 1
				else :
					bulls = bulls + 1
			print( f'cows = {cows} and bulls = {bulls}' )
			if( 4 == cows ) :
				print( 'You got the 4 cows, number is correct' )
				sys.exit()

if __name__ == '__main__' :
	cowsnbulls()
##########
#cut_rectangle_in_min_sq.py
##########
# 36 - 2,3,4,6,9,12,18
# 30 - 2,3,5,6,10,15

def handleCalculateSquares( height, width ) :

	while height != width and 0 not in [height, width] :
		if height == width :
			print( '1 square of' + str(height) )
		elif height < width :
			print ( str(width // height) + ' squares of ' + str( height ) )
			height, width = width % height, height
		else :
			print (str(height // width) + ' squares of ' + str( width ))
			width, height = height % width, width

handleCalculateSquares( 30, 36 )
print('-'*10)
handleCalculateSquares( 13, 29 )
##########
#date_time.py
##########
from datetime import datetime
from datetime import timedelta

strDateTime = datetime(2016,1,1) + timedelta(days=255)

print( str(strDateTime.day) + '/' + str(strDateTime.month) + '/' + str(strDateTime.year) )
##########
#decode_web_page.py
##########
import requests
import bs4

strLink = 'https://www.nytimes.com'

response = requests.get( strLink )
html = response.text

soup = bs4.BeautifulSoup( html, 'html.parser' )

strContent = soup.find( id="site-content")

for div in strContent.find('div') :
	if None != div:
		print(div.get_text())
##########
#divisors.py
##########
intnumber = int( input( 'Enter number ' ) )

for i in range( 1, ( intnumber//2 ) + 1 ) :
	if( 0 == intnumber % i ) :
		print( i )
##########
#draw_a_game_board.py
##########
plot_range = int( input( 'Enter range : ' ) )
verticle = '|   '
horizontal = ' ---'

for i in range( plot_range ) :
	print( horizontal * plot_range )
	print( verticle * ( plot_range + 1 ) )
print( horizontal * plot_range )
##########
#element_search.py
##########
lstNumbers = [1, 2, 3, 4, 5, 6, 7, 9, 12, 19, 23, 24, 43, 45, 54, 78, 87, 98, 123, 234, 457, 654, 723, 856, 942, 967, 998]
inputnumber = int( input( 'Enter number : ' ) )

while( 1 ) :
	start = 0
	middle = len( lstNumbers ) // 2
	end = len( lstNumbers )

	if( 2 == len( lstNumbers ) ) :
		if( inputnumber in lstNumbers ) :
			print( 'Found it' )
		else :
			print( 'Nope not there' )
		# found = 1
		break
	if inputnumber > lstNumbers[middle] :
		lstNumbers = lstNumbers[middle:end]
		# print(lstNumbers)
	else :
		lstNumbers = lstNumbers[start:middle]
		# print(lstNumbers)

##########
#fibonacci.py
##########
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
##########
#file_names.py
##########

##########
#file_overlap.py
##########
with open( 'primenumbers.txt', 'r' ) as prime_numbers_file :
	prime_numbers = (prime_numbers_file.readlines())

with open ( 'happynumbers.txt', 'r' ) as happy_numbers_file :
	happy_numbers = happy_numbers_file.readlines()

for i in prime_numbers :
	for j in happy_numbers :
		if( i == j ) :
			print( i.strip( '\n' ) )
##########
#guessing_game_1.py
##########
import sys
import random

tries = 0
secret_number = random.randint( 1, 9 )

while( 1 ) :
	user_input = input( 'Guess the number or press "q" to quit : ' )
	if( 'q' == user_input ) :
		print( f' Total tries : {tries} and correct number is {secret_number}')
		sys.exit()
	else :
		tries = tries + 1
		user_input = int( user_input )
		if( user_input == secret_number ) :
			print( 'There you are!' )
			print( f' Total tries : {tries}')
			sys.exit()
		elif( user_input < secret_number ) :
			print( 'Too low!' )
		else :
			print( 'To high!' )
##########
#guessing_game_2.py
##########
import sys
import random

print( 'Keep number in your head between 1 to 100, I will guess the nuber' )

guess_attempts = 1

start = 1
end = 100
middle = end // 2

while( 1 ) :

	middle = (start+end) // 2

	print( f'{start}, {middle}, {end}' )

	print( f'number is {middle}' )

	userinput = int( input( 'Press "1" for high, "2" for low, 3 for correct answer and 4 to quit : ' ) )
	if( 4 == userinput or 3 == userinput ) :
		print( f'Guesses = {guess_attempts}')
		sys.exit()
	elif( 1 == userinput ) :
		guess_attempts = guess_attempts + 1
		end = middle
	else :
		guess_attempts = guess_attempts + 1
		start = middle
##########
#hackerrank_alphabets_rangoli.py
##########
import string

def print_rangoli(size):
	lstAlphabets = list(string.ascii_lowercase)[:size]
	lstAlphabets.reverse()
	lstPattern = []
	i = (size*2) - 2
	j = 0
	while i >= 0 :
		lstMiddlePattern = []
		strPattern = '-' * (i)
		# print(strPattern, end='')
		for k in range(0,j+1) :
			lstMiddlePattern.append( lstAlphabets[k] )
		l = j - 1
		while l >= 0 :
			lstMiddlePattern.append( lstAlphabets[l] )
			l = l - 1
		strPattern = strPattern + '-'.join( lstMiddlePattern )
		strPattern = strPattern + '-' * (i)
		i = i - 2
		j = j + 1
		print(strPattern)
		lstPattern.append(strPattern)
	lstPattern.pop()
	for i in lstPattern[::-1] :
		print(i)
if __name__ == '__main__':
	n = int(input())
	print_rangoli(n)
##########
#hackerrank_birthday_candles.py
##########
from itertools import groupby

if __name__ == '__main__' :
	n = int(input())
	totalCandles = list(map(int,input().rstrip().split()))
	totalCandles.sort(reverse = True )
	totalCandles = groupby(totalCandles)
	for i,j in totalCandles :
		print(len(list(j)))
		break
##########
#hackerrank_check_valid_string.py
##########
n = int(input('enter number : '))

for i in range(n) :

	strUid = input('enter string : ')

	lstUid = set(list(strUid))
	intCount = 0
	strUpCount = 0

	if strUid.isalnum() and 10 == len(lstUid):
		for inputchar in strUid :
			if inputchar.isdigit() :
				intCount = intCount + 1
			if inputchar.isupper() :
				strUpCount = strUpCount + 1

	if 2 <= strUpCount and 3 <= intCount :
		print( 'Valid' )
	else :
		print( 'Invalid' )
##########
#hackerrank_chocolate_bar.py
##########
def birthday(s, d, m):

	intTotalWays = 0
	# print( len(s) - m)
	for i in range( len(s) ):
		# print(i)
		nextValSum = 0
		for j in range(m) :
			if i+j < len(s) :
				nextValSum = nextValSum + s[i+j]
		if nextValSum == d :
			intTotalWays = intTotalWays + 1

	return intTotalWays


if __name__ == '__main__':
	n = int(input().strip())
	s = list(map(int, input().rstrip().split()))
	dm = input().rstrip().split()
	d = int(dm[0])
	m = int(dm[1])
	result = birthday(s, d, m)
	print(result)
##########
#hackerrank_cloud_jumps.py
##########
if __name__ == '__main__' :
	n = int(input())
	lstNumbers = list(map(int,input().split()))
	intPosition = 0
	intJumpCount = 0

	while intPosition < len(lstNumbers)-2 :
	# for intPosition in range(0,len(lstNumbers)-2) :
		# print(intPosition)
		# if 1 != lstNumbers[intPosition] :
		if 0 == lstNumbers[intPosition] and 0 == lstNumbers[intPosition+2] :
			# print( '--1--', end = ' ')
			# print(intPosition)
			intPosition = intPosition + 2
			intJumpCount = intJumpCount + 1
		elif 0 == lstNumbers[intPosition] and 0 == lstNumbers[intPosition+1] and 1 == lstNumbers[intPosition+2] :
			# print( '--2--', end = ' ')
			# print(intPosition)
			intPosition = intPosition + 1
			intJumpCount = intJumpCount + 1
		else :
			intPosition = intPosition + 1

	if 0 == lstNumbers[len(lstNumbers)-2] :
		intJumpCount = intJumpCount + 1

	print(intJumpCount)
##########
#hackerrank_compare_triplets.py
##########
# Complete the compareTriplets function below.
def compareTriplets(a, b):
	ascore = 0
	bscore = 0
	for i in range(len(a)) :
		if a[i] > b[i] :
			ascore = ascore + 1
		elif a[i] < b[i] :
			bscore = bscore + 1
	return f'{ascore} {bscore}'

if __name__ == '__main__':
	a = list(map(int, input().rstrip().split()))

	b = list(map(int, input().rstrip().split()))

	result = compareTriplets(a, b)
	print(result)
##########
#hackerrank_day_in_programers_life.py
##########
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__' :
	intYear = int(input())
	days = 255

	if intYear < 1919 and intYear % 4 == 0 and intYear % 100 == 0:
		days = 254
	if intYear == 1918 :
		days = 268

	strDate = datetime.strftime(datetime(intYear,1,1) + timedelta(days=days), "%d.%m.%Y")
	print(strDate)
##########
#hackerrank_default_argument.py
##########
lstNumbers = []
class EvenStream(object):
	def __init__(self):
		self.current = 0

	def get_next(self):
		to_return = self.current
		self.current += 2
		return to_return

class OddStream(object):
	def __init__(self):
		self.current = 1

	def get_next(self):
		to_return = self.current
		self.current += 2
		return to_return

def print_from_stream1(n, stream=EvenStream()):
	lstNumbersFromStream = []
	for _ in range(n):
		yield(stream.get_next())

def print_from_stream(n, stream=EvenStream()):
	lstNumbers.append( print_from_stream1(n, stream) )


queries = int(input())
for _ in range(queries):
	stream_name, n = input().split()
	n = int(n)
	if stream_name == "even":
		print_from_stream(n)
	else:
		print_from_stream(n, OddStream())

for i in list(lstNumbers) :
	for j in list(i) :
		print(j)
##########
#hackerrank_divisible_sum_pairs.py
##########
if __name__ == '__main__' :
	nk = list(map(int, input().strip().split()))
	intDivisor = nk[1]
	lstNumbers = list(map(int, input().strip().split()))

	print( ([(i,j) for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0]) )
##########
#hackerrank_door_mat.py
##########
if __name__ == '__main__' :
	mn = list(map(int,input().strip().split()))
	m = mn[0]
	n = mn[1]
	j = 2
	strlstLines = []
	for i in range( 1, m, 2 ):
		dashes = ( n - ( i*3 ) ) // 2
		strLine = '-' * dashes
		strLine = strLine + '.|.' * i
		strLine = strLine + '-' * dashes
		print(strLine)
		strlstLines.append(strLine)
	print( '-' * ( ( n - 7 ) // 2 ) + 'WELCOME' + '-' * ( ( n - 7 ) // 2 ) )
	strlstLines.reverse()
	for i in strlstLines :
		print(i)
##########
#hackerrank_find_avrage.py
##########
if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores
	query_name = input()

	for name, marks in student_marks.items():
		total = 0
		for mark in marks :
			total = total + mark
		student_marks[name] = total/3
	print( "%.2f" % student_marks[query_name] )
##########
#hackerrank_find_string.py
##########
def count_substring(strParent, strSubString):
	i = 0
	totalMatches = 0
	while i < len(strParent) :
		intPosition = strParent.find(strSubString)
		if -1 != intPosition :
			totalMatches = totalMatches + 1
			strParent = strParent[intPosition+1:]
		else :
			break

	return totalMatches

if __name__ == '__main__' :
	strParent = input().strip()
	strSubString = input().strip()
	count = count_substring(strParent, strSubString)
	print(count)

##########
#hackerrank_grading_student.py
##########
if __name__ == '__main__':
	n = int(input())
	grades = []
	for _ in range(n):
		grades_item = int(input())
		grades.append(grades_item)
	for grade in grades :
		roundedGrade = grade + 5 - grade%5
		if ( roundedGrade - grade ) < 3 and roundedGrade >= 40 :
			print( roundedGrade )
		else :
			print( grade )
##########
#hackerrank_itertools.py
##########
from itertools import combinations_with_replacement
strWord = input()
strWord = strWord.split()
intNumber = int(strWord[1])
strWord = list(strWord[0])

if True == ''.join(strWord).isupper() and 0 < intNumber and intNumber <= len(strWord) :
	strWord.sort()
	for i in combinations_with_replacement( strWord, intNumber ) :
		print(''.join(i))
##########
#hackerrank_itertools_groupby.py
##########
from itertools import groupby
strInput = input()

if strInput.isdigit() :
	for i,j in groupby(strInput) :
		print( '(' + str( len( list( j ) ) ) + ', ' + str(i) + ')', end = ' ' )
##########
#hackerrank_itertools_product.py
##########
from itertools import product

if __name__ == '__main__' :
	list1 = map( int, input().split() )
	list2 = map( int, input().split() )

	for i in product(list1, list2) :
		print( i, end = ' ' )
##########
#hackerrank_kangaroo.py
##########
import sys
def kangaroo(x1, v1, x2, v2):

	for i in range(10000) :
		if x1 == x2 :
			print('YES')
			sys.exit()
		x1 = x1 + v1
		x2 = x2 + v2

	print('NO')


if __name__ == '__main__':

	arrNumbers = list(map(int, input().strip().split()))
	x1 = arrNumbers[0]
	v1 = arrNumbers[1]
	x2 = arrNumbers[2]
	v2 = arrNumbers[3]
	if x1 < x2 and v1 < v2 :
		print('NO')
	else :
		result = kangaroo(x1, v1, x2, v2)
##########
#hackerrank_knight_moves.py
##########
x = 3
y = 3

for i in range(8) :
	for j in range(8) :
		if (x-i in [2,-2] and y-j in [1,-1]) or (x-i in [1,-1] and y-j in [2,-2]) :
			print(i,j)
##########
#hackerrank_list_comprehensions.py
##########
if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

print( [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ] )
##########
#hackerrank_list_left_rotation.py
##########
def rotLeft( oldList, intRotations ):
	newList = oldList.copy()
	intListLength = len(oldList)
	intShiftPosition = len(oldList) - intRotations
	i = 0
	while i < intRotations :
		newList[i+intShiftPosition] = oldList[i]
		i = i + 1
	i = 0
	while i < intShiftPosition :
		newList[i] = oldList[intRotations+i]
		i = i + 1
	return newList

if __name__ == '__main__':

	nd = input().split()

	n = int(nd[0])

	d = int(nd[1])

	a = list(map(int, input().rstrip().split()))

	result = rotLeft(a, d)
	print( ' '.join( str(i) for i in result ) )
##########
#hackerrank_list_operations.py
##########
if __name__ == '__main__':
	lstOperations = ['insert','remove','append','sort','pop','reverse','print']
	lstNumbers = []
	n = int(input())
	for _ in range(n) :
		strOperation, *lstOpNumbers = input().split()
		lstOpNumbers = list(map(int,lstOpNumbers))
		if( strOperation in lstOperations ) :
			if( 'insert' == strOperation ) :
				lstNumbers.insert( lstOpNumbers[0], lstOpNumbers[1] )
			elif( 'remove' == strOperation ) :
				lstNumbers.remove(lstOpNumbers[0])
			elif( 'append' == strOperation ) :
				lstNumbers.append(lstOpNumbers[0])
			elif( 'sort' == strOperation ) :
				lstNumbers.sort()
			elif( 'pop' == strOperation ) :
				lstNumbers.pop()
			elif( 'reverse' == strOperation ) :
				lstNumbers.reverse()
			else :
				print( lstNumbers )
##########
#hackerrank_mean_var_std.py
##########
import numpy as np

if __name__ == '__main__' :
	lstNumbers=[]
	n, m = map(int,input().split())
	for _ in range( n ) :
			lstNumbers.append(list(map(int,input().split())))
	lstNumbers = np.array(lstNumbers)
	print( np.mean(lstNumbers, axis = 1 ) )
	print( np.var(lstNumbers, axis = 0 ) )
	print( np.std(lstNumbers, axis = None ) )
##########
#hackerrank_merge_the_tools.py
##########
from collections import OrderedDict

def merge_the_tools(string, k):
	i = 0
	while i < len(string) :
		print( ''.join( list( OrderedDict.fromkeys( string[i:i+k] ) ) ) )
		i = i + k

if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools(string, k)
##########
#hackerrank_migratory_birds.py
##########
from itertools import groupby

def migratoryBirds(arr):
	arr.sort()
	intCount = 0
	for i, j in groupby(arr) :
		inTotalCount = len(list(j))
		if intCount < inTotalCount :
			intCount = inTotalCount
			intNumber = i
	print(intNumber)

if __name__ == '__main__':
	arr_count = int(input().strip())
	arr = list(map(int, input().rstrip().split()))
	result = migratoryBirds(arr)

##########
#hackerrank_minions.py
##########
def minion_game(string):
	string = string.lower()
	kevin = 0
	stuart = 0
	for i in range(len(string)) :
		if string[i] in ['a','e','i','o','u'] :
			# kevin = kevin + len(string[i:])
			kevin = kevin + (len(string)-i)
		else :
			# stuart = stuart + len(string[i:])
			stuart = stuart + (len(string)-i)

	if kevin > stuart :
		print( f"Kevin {kevin}" )
	elif kevin < stuart :
		print( f"Stuart {stuart}" )
	else :
		print( 'Draw' )

if __name__ == '__main__':
	s = input().lower()
	minion_game(s)
##########
#hackerrank_mutable_Strings.py
##########
def mutate_string( strInput, intIndex, strChar):
	strInput = list(strInput)
	strInput[intIndex] = strChar
	return ''.join(strInput)


if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)
##########
#hackerrank_nested_lists.py
##########
from itertools import groupby
from operator import itemgetter

if __name__ == '__main__':

	lstStudentGrades= []

	for _ in range(int(input())):
		name = input()
		score = float(input())
		lstStudentGrades.append([name,score])

	lstStudentGrades.sort( key = lambda x : x[1] )
	y = groupby(lstStudentGrades, lambda x: x[1])

	intCount = 1
	for i,j in y:
		if 2 == intCount :
			lstNames = [x[0] for x in list(j)]
			lstNames.sort()
			for strName in lstNames :
				print( strName )
			break
		intCount = intCount + 1
##########
#hackerrank_new_year_chaos.py
##########
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	pass

if __name__ == '__main__':
	t = int(input())

	for t_itr in range(t):
		n = int(input())

		q = list(map(int, input().rstrip().split()))

		minimumBribes(q)

##########
#hackerrank_plus_minus.py
##########
#!/bin/python3
# Complete the plusMinus function below.
def plusMinus(arr):

	intTotalPositive = 0
	intTotalNegative = 0
	intTotalZeros = 0

	for i in arr:
		if i < 0 :
			intTotalNegative = intTotalNegative + 1
		elif i > 0 :
			intTotalPositive = intTotalPositive + 1
		else :
			intTotalZeros = intTotalZeros + 1

	print( "{0:.6f}".format(round(intTotalPositive/len(arr),6)) )
	print("{0:.6f}".format(round(intTotalNegative/len(arr),6)))
	print( "{0:.6f}".format(round(intTotalZeros/len(arr),6)) )

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	plusMinus(arr)
##########
#hackerrank_repeated_strings.py
##########
if __name__ == '__main__':
	s = input()
	n = int(input())

	intTotalCountOfFirstChar = s.count("a")
	intTotalOccurances = ( n // len(s) * intTotalCountOfFirstChar )
	intTotalOccurances = intTotalOccurances + s[:n%len(s)].count("a")
	print(intTotalOccurances)
##########
#hackerrank_runner_up.py
##########
if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	arr = list(arr)
	arr = list(set(arr))
	arr.sort()
	print(arr[-2])
##########
#hackerrank_set.py
##########
if __name__ == '__main__' :
	s = set()
	n = int(input())
	for _ in range(n) :
		strCountry = input()
		s.add(strCountry)
	print(len(s))
##########
#hackerrank_sock_merchant.py
##########
from itertools import groupby

def sockMerchant(n, ar):
	ar = groupby( ar )
	totalSocks = 0
	for i,j in ar :
		totalSocks = totalSocks + len( list( j ) ) // 2
	return totalSocks

if __name__ == '__main__':
	n = int(input())
	ar = list(map(int, input().rstrip().split()))
	ar.sort()
	totalSocks = sockMerchant(n, ar)

	print( totalSocks )
##########
#hackerrank_staircase.py
##########
if __name__ == '__main__':
	n = int(input())
	for i in range(1,n+1) :
		print( ''.rjust(n-i) + '#'*i )
##########
#hackerrank_string_formatting.py
##########
if __name__ == '__main__' :
	n = int(input())
	width = len(bin(n)[2:])
	for i in range( 1, n + 1 ) :
		print( str(i).rjust(width, ' '), end = ' ' )
		print(oct(i)[2:].rjust(width, ' '), end = ' ' )
		print(str(hex(i)).upper()[2:].rjust(width, ' '), end = ' ' )
		print(bin(i)[2:].rjust(width, ' '))
##########
#hackerrank_string_ops.py
##########
import re
if __name__ == '__main__':
	s = input()
	if( 0 != len(list(re.findall( '[0-9a-zA-Z]', s )) )):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[a-zA-Z]', s )) )) :
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[0-9]', s )) ) ):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[a-z]', s )) ) ):
		print( True )
	else :
		print( False )
	if( 0 != len(list(re.findall( '[A-Z]', s )) ) ):
		print( True )
	else :
		print( False )
##########
#hackerrank_textwrap.py
##########
import textwrap

def wrap(string, max_width):
	return textwrap.fill(string,max_width)

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)
##########
#hackerrank_text_alignment.py
##########
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
	print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

#Top Pillars
for i in range(thickness+1):
	print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
	print((c*thickness*5).______(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
	print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

#Bottom Cone
for i in range(thickness):
	print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
##########
#hackerrank_timeconversion.py
##########
from datetime import datetime

if __name__ == '__main__' :
	strTime = input()
	print( datetime.strftime( datetime.strptime( strTime, "%I:%M:%S%p" ), "%H:%M:%S" ) )
##########
#hackerrank_title_word.py
##########
import string
def solve(s):
	return string.capwords(s, ' ')
	# lst = []
	# for i in s.split() :
	# 	print(i)
	# 	lst.append( i.capitalize() )
	# return ' '.join( lst )

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	print(solve(s))

	# fptr.write(result + '\n')

	# fptr.close()
##########
#hackerrank_tuple_hash.py
##########
print(hash((1,2)))
##########
#hackerrank_valley_count.py
##########
from itertools import groupby
if __name__ == '__main__':
	n = int(input())
	lstSteps = list(input())
	valleycount = 0
	previous = ''
	for i,j in groupby(lstSteps) :
		if 'D' == previous and 'U' == i and 1 < len(list(j)) :
			valleycount = valleycount + 1
		previous = i
	print(valleycount)

# This script has failed exam.
##########
#juice_stalls.py
##########
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


##########
#lamdba_functions.py
##########
# f = lambda x,y : return x + y

f = lambda x : x*x
lstNumbers = [1,2,3,4,5]

print( [f(i) for i in lstNumbers] )

x = map( f, lstNumbers )

print(list(x))


def filtereven( i ):
	if 0 == i % 2 :
		return True
	return False

x = filter( filtereven, lstNumbers)
print(list(x))

def filterodd() :
	lstNumbers = [1,2,3,4,5]
	for i in lstNumbers :
		if 1 == i % 2 :
			yield i

x = filterodd()
for i in x:
	print( i )
##########
#list_all_files_n_contents.py
##########
import os

objFile = open( 'new_file.py', 'w' )

for file_name in os.listdir('./') :
	if file_name.endswith( '.py' ) :
		objFile.write( '#'*10 )
		objFile.write( file_name )
		objFile.write( '#'*10 )
		with open( file_name, 'r' ) as file_to_read :
			line = file_to_read.readline()
			while line :
				objFile.write( line )
				line = file_to_read.readline()


objFile.close()
##########
#list_comprehensions.py
##########
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Print even numbers
print( [i for i in a if 0 == i % 2] )
##########
#list_less_than_ten.py
##########
lstintNumbers = [1,2,5,765,763,3456,7,5632,123,87654,4565,4]
print( [ i for i in lstintNumbers if i > 10 ] )
##########
#list_overlap.py
##########
from random import randint

lstintRandom1 = range( 0, randint( 1, 100 ) )
lstintRandom2 = range( 0, randint( 1, 100 ) )

print( lstintRandom1 )
print( lstintRandom2 )

print( [ i for i in lstintRandom1 if i in lstintRandom2 ] )
##########
#list_overlap_comprehensions.py
##########
import random

listA = random.sample( range( 100 ), 15 )
listB = random.sample (range( 100 ), 20 )

print(listA)
print(listB)

print( [ i for i in set(listA) if i in set(listB)] )
##########
#list_remove_duplicates.py
##########
lstNumbers = [1,2,3,4,5,6,7,9,9,987,4,234,5,3456,2,1,234,6,2,112,34,56,2,2345,2,345,6,2,334,43,123,4,45,3]

print(len((lstNumbers)))
print((list(set(lstNumbers))))

lstNew = []
for i in lstNumbers :
	if( i not in lstNew ):
		lstNew.append(i)

print(lstNew)
##########
#matrix_and_transpose.py
##########
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
##########
#odd_or_even.py
##########
number = input( 'Gimmie number ' )
if False == number.isdigit() :
	print( 'You didn\'t give integer, bye!' )
else :
	number = int( number )
	if 0 == number % 2:
		print( 'It is even' )
	else :
		print( 'It is odd' )
##########
#password_generator.py
##########
import random
import string

password = ''
password = password + ''.join( random.sample( string.ascii_lowercase, 5) )
password = password + ''.join( random.sample( string.ascii_uppercase, 5 ) )
password = password + ''.join( random.sample( string.digits, 6 ) )
password = password + ''.join( random.sample( string.punctuation, 4 ) )

password = list( password )
random.shuffle( password )

print( ''.join( password ) )
##########
#program1.py
##########
from itertools import groupby
def findDifferentWays(size, allowedChanges, str):

	lstNumbers = list(map(int, list(str) ))

	lstNumbers.sort()

	lstLengths = []
	for i,j in groupby(lstNumbers) :
		lstLengths.append( len(list(j)) )

	# print(lstLengths)
	numofZeros = lstLengths[0]
	numofOnes = lstLengths[1]

	if allowedChanges < numofZeros :
		return (numofOnes - allowedChanges)
	elif allowedChanges == numofZeros :
		return numofZeros-numofOnes
	else :
		return allowedChanges


print(findDifferentWays(7,1,'1010101'))
print(findDifferentWays(5,3,'01010'))
##########
#program2.py
##########

##########
#read_from_file.py
##########
names = {}
with open( 'names.txt', 'r' ) as open_file :
	line = open_file.readline()
	while line :
		line = line.strip( '\n' )
		if line not in names :
			# names.append( line )
			names[line] = 1
		else :
			names[line] = names[line] + 1
		# print(line)
		line = open_file.readline()
print(names)
##########
#read_from_json.py
##########
import json
from datetime import datetime
import matplotlib.pyplot as plt

months = {}

with open( 'json_file.json' ) as json_file :
	line = json_file.read()
	line = json.loads( line )
	for i in line :
		jsondate = line[i].split('/')
		datem = datetime( int(jsondate[2]), int(jsondate[0]), int(jsondate[1]) ).strftime('%b')
		if( datem not in months ) :
			months[datem] = 1
		else :
			months[datem] = months[datem] + 1

plt.bar( months.keys(), months.values() )
plt.show()
##########
#regex.py
##########
import re

strLine = "The rain in Spain"

# findall - prints all matches, returns "None" otherwise
lstMatches = re.findall( "ai", strLine )
print( lstMatches )

lstMatches = re.findall( "[\a-z]", strLine )
print( lstMatches )

# search - it searches for the match and if there are more than one match first one is returned returns "None" otherwise

lstMatches = re.search( 'rain', strLine )

print( lstMatches.start() )

# split - returns the list, where the string splits at match
lstMatches = re.split( 'ain', strLine )
print( lstMatches )

# sub - replaces every match with given string
lstMatches = re.sub( "\s", "9", strLine )
print( lstMatches )

ip = "7.0.0.1"
strMatches = re.findall( "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip )
print(strMatches)

for i in range(1,10) :
	print(i)
##########
#reverse_word_order.py
##########
strName = 'My name is Michael'

strName = ' ' .join(strName.split()[ : : -1])
print( strName )
##########
#rock_scissor_paper.py
##########
quit_game = False
while False == quit_game :
	user_input = input( 'Enter "q" to quit the game or press enter to continue game ' )
	if "q" == user_input :
		print( 'Bye!' )
		quit_game = True
	else :
		player_1 = int( input( 'Player 1, enter your weapon no. \n 1. Rock \n 2. Scissor \n 3. Paper : ' ) )
		player_2 = int( input ( 'Player 2, enter your weapon no. \n 1. Rock \n 2. Scissor \n 3. Paper : ' ) )

		if( player_1 == player_2 ) :
			print( 'Tied!!' )
		elif( 1 == player_1 ) :
			if( 2 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
		elif( 2 == player_1 ) :
			if( 3 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
		elif( 3 == player_1 ) :
			if( 1 == player_2 ) :
				print( 'Winner: Player 1' )
			else :
				print( 'Winner: Player 2' )
##########
#string_functions.py
##########
# Capitalize first letter of string
strLine = 'this is text'
print( strLine.capitalize() )

# title - Convert first character of the word to upper in given string
print( strLine.title() )

# Upper - convert to uppercase
print( strLine.upper() )

# Lower - convert to lowercase
print( strLine.lower() )

# Casefold - convert to lowercase - simmilar to lower
print( strLine.casefold() )

# Swapcase - Swap the case of string
strLine = 'ThIs Is TeXt'
print( strLine.swapcase() )

# Count - Count the string occurances in given string
strLine ='I love apples, apple are my favorite fruit'
print( strLine.count( 'apple' ) )
print( strLine.count( 'e' ) )

#Startswith - returns true if it starts with given letter - This is case sensitive
print( strLine.startswith( 'i' ) )
print( strLine.startswith( 'I' ) )

#Endswith - returns true if it string ends with given character - Case sensitive function
print( strLine.endswith('t') )
print( strLine.endswith('T') )

# Find - finds the given string in string and returns position of first occurance else -1
print( strLine.find( 'apple' ) )

# Index - Returns the location of the searched string, in given string else raises exception
print( strLine.index( 'apple' ) )

#isalpha - Checks if the string has all letters
strLine = 'Test'
print( strLine.isalpha() )

# isalnum - check if the string is alphanumeric
strLine = 'Test123'
print( strLine.isalnum() )

# isdigit - Checks if string has all digits
strLine = '12345'
print( strLine.isdigit() )

# isdecimal - Checks if all characters are decimals
strLine = '12345'
print( strLine.isdecimal() )

# isnumeric - Checks if all characters are numeric
strLine = '1234567'
print( strLine.isnumeric() )

# islower - Checks if all character are lower
strLine = 'test'
print( strLine.islower() )

# isupper - Checks if all characters are upper
strLine = 'TEST'
print( strLine.isupper() )

# join - joins the list items by a seperator
lstNames = ['one', 'two', 'three', 'four']
print( ' & '.join( lstNames ) )

# split - Split the string by seperator and converts it to list
strLine = '&'.join( lstNames )
print( strLine.split( '&' ) )

# replace - replace the substrings by given string
strLine ='I love apples, apples are my favorite fruit'
strLine = strLine.replace( 'apples', 'mangoes' )
print( strLine )

# lstrip - strip spaces/characters from left of the string
strLine ='        Banana             Apple'
print( strLine.lstrip() )

# rstrip - strip spaces/characters from right of the string
strLine ='Apple        Banana             '
print( strLine.rstrip() )

# rfind - find last occurance of substring in a given string
strLine ='I love apples, apples are my favorite fruit'
print( strLine.rfind( 'apple' ) )

# rsplit - will start splitting from right and max is the number how many parts to b
# e split into, if not given it works as split()
strLine ='I love apples, apples are my favorite fruit'
print( strLine.rsplit( ' ', 2 ) )

# splitline - Split the string where new line is given
strLine = "Thank you for the music\nWelcome to the jungle"
print(strLine.splitlines())


# zfill - insert the zeros at begining of the string till it reaches the length
strLine = 'Zero'
print( strLine.zfill( 10 ) )

# pad with characters
strLine = 'One'
print(strLine.ljust(5,'1'))
print(strLine.rjust(5,'1'))


strLine = 1
print( strLine.isdigit() )

##########
#test.py
##########
import os
lstFiles = (list(os.listdir('./')))
with open('file_names.py', 'w') as writefile :
	for filename in lstFiles:
		if filename.endswith('.py') :
			print( filename )
			writefile.write('\n'+'#'*10+'\n')
			writefile.write('#'+filename+'\n')
			writefile.write('#'*10+'\n')
			with open( filename, 'r' ) as readfile:
				# writefile.writelines(readfile.readlines())
				for line in readfile.readlines() :
					writefile.write(line)
##########
#write_to_file.py
##########
with open( 'writetofile.txt', 'w' ) as open_file:
	for i in range(10) :
		open_file.writelines( str(i) )
##########
#write_to_json.py
##########
import json

birthdays = {
		'Albert Einstein': '03/14/1879',
		'Benjamin Franklin': '01/17/1706',
		'Ada Lovelace': '12/10/1815',
		'Donald Trump': '06/14/1946',
		'Rowan Atkinson': '01/6/1955'}

with open( 'json_file.json', 'a' ) as json_file :
	json_file.writelines( json.dumps( birthdays ) )
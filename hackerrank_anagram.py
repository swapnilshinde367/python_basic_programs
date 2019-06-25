#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):

	if len(s)%2 != 0 :
		return -1

	str1 = list(s[:len(s)//2])
	str2 = list(s[len(s)//2:])
	str1.sort()
	str2.sort()

	print(str1)
	print(str2)

	if str1 == str2 :
		return 0

	return len([ ch1 for ch1 in str1  if ch1 not in str2 ])

if __name__ == '__main__':

	q = int(input())

	for _ in range(q):
		s = input()
		result = anagram(s)
		print(result)

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
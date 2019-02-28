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
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
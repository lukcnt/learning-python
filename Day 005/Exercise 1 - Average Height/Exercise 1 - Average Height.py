student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

totalHeight = 0
totalStudents = 0

for i in student_heights:
  totalHeight += i
  totalStudents += 1

print(round(totalHeight / totalStudents))
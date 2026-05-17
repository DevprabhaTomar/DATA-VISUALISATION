# File Name: student_marks.py

# Create and write data to file
file = open("marks.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    file.write(name + " " + str(marks) + "\n")

file.close()

# Read file
file = open("marks.txt", "r")

students = []
total = 0

for line in file:
    data = line.split()
    name = data[0]
    marks = int(data[1])

    students.append((name, marks))
    total += marks

file.close()

average = total / len(students)

# Find topper
topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

print("\nTopper:", topper[0], "-", topper[1])

print("Average Marks:", average)

print("\nStudents scoring below average:")

for student in students:
    if student[1] < average:
        print(student[0], "-", student[1])
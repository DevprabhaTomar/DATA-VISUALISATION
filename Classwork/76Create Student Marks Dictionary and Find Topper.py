#Create Student Marks Dictionary and Find Topper
def find_topper(student_marks):
    topper = max(student_marks, key=student_marks.get)
    return topper, student_marks[topper]

# Read number of students
n = int(input())

student_marks = {}
for _ in range(n):
    name, marks = input().split()
    student_marks[name] = int(marks)

# Print topper
name, marks = find_topper(student_marks)
print(f"Topper: {name} with marks {marks}")

#Input:

3
Alice 85
Bob 92
Charlie 88

#Output: Topper: Bob with marks 92
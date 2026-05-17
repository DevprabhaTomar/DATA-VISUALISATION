# File Name: grading_system.py

# Input marks of 5 subjects
total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

# Calculate percentage
percentage = total / 5

print("Percentage:", percentage)

# Assign grade using nested if-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# Scholarship eligibility
if percentage >= 85:
    print("Scholarship Qualified")
else:
    print("Not Qualified for Scholarship")
course1 = [("Aman", "Python"), ("Ravi", "Java"), ("Sita", "Python")]
course2 = [("Aman", "Java"), ("Neha", "Python"), ("Ravi", "C++")]

set1 = set([name for name, course in course1])
set2 = set([name for name, course in course2])

common_students = set1.intersection(set2)

print("Students in multiple courses:", common_students)
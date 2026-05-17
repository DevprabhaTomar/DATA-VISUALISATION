# File Name: set_operations.py

set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")
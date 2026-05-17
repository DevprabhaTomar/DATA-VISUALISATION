# File Name: merge_lists.py

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

# Merge lists
merged = list1 + list2

# Remove duplicates
unique_list = []

for num in merged:
    if num not in unique_list:
        unique_list.append(num)

# Sort in descending order
for i in range(len(unique_list)):
    for j in range(i + 1, len(unique_list)):
        if unique_list[i] < unique_list[j]:
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]

# Display numbers divisible by both 3 and 5
print("Numbers divisible by both 3 and 5:")

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
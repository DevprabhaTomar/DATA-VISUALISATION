# File Name: second_largest_smallest.py

def find_elements(numbers):

    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in numbers:

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest


nums = list(map(int, input("Enter numbers separated by space: ").split()))

second_largest, second_smallest = find_elements(nums)

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
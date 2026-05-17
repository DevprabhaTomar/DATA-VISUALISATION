#creating a blank list
numbers = []
#to ask user to input number of elements to list
n = int(input("Enter number of elements in list : "))
#to ask user to input elements in list
for i in range(n):
    num=int(input())
    print("----------------------------------------------")
    #appending number in list
    numbers.append(num)
#dislpaying list 
print("Number in the list are : ", numbers)
#to find sum of all the numbers in the list
sum = 0
for num in numbers:
    sum += num
print("sum of all numbers in the list is :",sum)
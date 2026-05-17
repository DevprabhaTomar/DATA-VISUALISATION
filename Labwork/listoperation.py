#creating a numeric list of 5 numbers
numbers = [45,47,89,34,56]
#displaying list numbers
print("numbers are :",numbers)
print("------------------------")
#displaying data without square brackets
print("numbers are :")
print(*numbers)
#------------------------------
#dispalying elements by using for loop
print("-------------------------------")
print("numbers are :")
for num in numbers:
    print(num)
#------------------------------
#------finding number of elements in list------
#len(). it returns number of elements in list
length = len(numbers)
print("numbers of elements in the list:",len)
#displaying elements in reverse order by using forward indexing
print("----------------------------")
print("numbers in reverse order")
for index in range(length-1,-1,-1):
    print(numbers[index],end = " ,")
#finding sum of all the numbers in list
sum = 0
for num in numbers:
    sum = sum + num
print("\n-----------------------------")
print("sum of all the numbers in list : ",sum)

#finding greatest number in list
max = numbers[0]
for index in range(1,length):
    if(max > numbers[index]):
        max = numbers[index]
print("\n----------------------------------")
print("Greatest number in list : ",max)

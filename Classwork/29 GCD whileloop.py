a = int(input())
b = int(input())

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)

#input
5
6
#output
1
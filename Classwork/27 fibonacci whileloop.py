n = int(input())

a = 0
b = 1
count = 0

while count < n:
    print(a)
    temp = a + b
    a = b
    b = temp
    count += 1

    #input
    3
    #output
    0
    1
    1
    1
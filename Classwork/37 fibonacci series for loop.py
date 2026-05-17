n = int(input())

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

   # Input
     5

#Output

0
1
1
2
3
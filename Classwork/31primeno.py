n = int(input())

if n < 2:
    print("No Prime Numbers")
else:
    for num in range(2, n + 1):
        prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                prime = False
                break
            i += 1
        if prime:
            print(num)
         #input
         5
        #output
        2
        3
        5
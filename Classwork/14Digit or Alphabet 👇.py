#  Read input
ch = input("Enter a character: ")

# Take only first character (in case user types more)
ch = ch[0]

# Check
if ch >= '0' and ch <= '9':
    print("Digit")
elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("Alphabet")


    #output
    Enter a character: a
     Alphabet
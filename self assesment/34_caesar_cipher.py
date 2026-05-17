def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr(ord(char) + shift)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr(ord(char) - shift)
        else:
            result += char
    return result

msg = input("Enter message: ")
shift = 3

enc = encrypt(msg, shift)
print("Encrypted:", enc)

dec = decrypt(enc, shift)
print("Decrypted:", dec)
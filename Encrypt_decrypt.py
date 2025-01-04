import random
import string

# Generate possible characters and the shuffled key
#punctuation=special character @ % digits=0-9 and ascii=a z and  A Z
chars = " " + string.punctuation + string.digits + string.ascii_letters
#making character as a list so each string is a individual 
chars = list(chars)
#copying chars in key
key = chars.copy()
#shuffling key they are same as chars but in  different order
random.shuffle(key)

def encrypt():
    #taking plain text as input
    plain_text = input("Enter a plain text: ")
    cipher_text = ""
#for is used for indexing each individual element
    for letter in plain_text:
        if letter in chars:  # Ensure the letter exists in chars
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Preserve characters that are not in chars (if any)

    print(f"plain text : {plain_text}")
    print(f"cipher text: {cipher_text}")
#decrypt same as encrypt
def decrypt():
    cipher_text = input("Enter cipher_text: ")
    plain_text = ""

    for letter in cipher_text:
        if letter in key:  # Ensure the letter exists in key
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter  # Preserve characters that are not in key (if any)

    print(f"cipher text: {cipher_text}")
    print(f"plain text: {plain_text}")

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    choose = input("1 or 2: ")

    if choose == "1":
        encrypt()
    elif choose == "2":
        decrypt()
    else:
        print("Enter a valid choice!")

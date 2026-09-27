print("Password Generator")
import secrets
import string
def generate(n):
    password = ""
    for i in range(n):
        password += secrets.choice(string.ascii_lowercase)
    print("Generated password :" , password)
    return
def get_valid_length():
    length = True
    n = int(input("Please enter desired length : "))
    if n < 1: 
        length = False
    while (length == False):
        n = int(input("Error, Invalid length. Please enter a valid length :"))
        if n >= 1 :
            length = True
    return n

generate(get_valid_length())
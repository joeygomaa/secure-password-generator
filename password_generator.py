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
    n = int(input("Please enter desired length : "))

    while n<=0 :
        n = int(input("Error, Invalid length. Please enter a valid length :"))
        
    return n

generate(get_valid_length())
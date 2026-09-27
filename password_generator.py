print("Password Generator")
import secrets
import string
def generate(n):
    if n<1:
        print("Please enter valid length")
    else:
        password = ""
        for i in range(n):
            password += secrets.choice(string.ascii_lowercase)
        print("Generated password :" , password)
        return

n = int(input("Please enter password length : "))
generate(n)
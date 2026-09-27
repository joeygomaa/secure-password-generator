print("Password Generator")
import secrets
import string
def generate(n):
    password = ""
    for i in range(n):
        password += secrets.choice(string.ascii_lowercase)
    print("Generated password :" , password)


def get_valid_length():
    while True :
        n = input("Please enter desired length : ")
        try:
            n = int(n)
            while (n<=0) or (n>128):
                if n<=0 :
                    n = int(input("Error, Invalid length. Please enter a valid length :"))
                else  :
                    n = int(input("Character limit : 128. Please enter a valid length :"))

            return n
        
        except ValueError:
            print("That was not a number.")
        
    

generate(get_valid_length())
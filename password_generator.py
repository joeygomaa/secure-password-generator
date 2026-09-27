print("Password Generator")
import secrets
import string
def generate(n):
    password = ""
    for i in range(n):
        password += secrets.choice(string.ascii_lowercase)
    print("Generated password :" , password)


def get_valid_length():
    prompt =  "Please enter desired length : "
    while True :
        n = input(prompt)
        try:
            n = int(n)
            if n <= 0 :
                prompt = "Error.Invalid number.Please enter a valid number :"
            elif n>128 :
                prompt = "Character limit : 128. Please enter a smaller number :"
            else:
                return n
            
        except ValueError:
            prompt = "That was not an integer. Try again :"
            continue
        
    

generate(get_valid_length())
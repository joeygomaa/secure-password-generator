import secrets
import string
import re
import math
from itertools import combinations

CHARACTER_TYPES = {
    "low": string.ascii_lowercase,
    "up" : string.ascii_uppercase,
    "num" : string.digits,
    "sym" : string.punctuation
}


def generate(n,selection):
    
    invalid = True

    while invalid :

        characters = ""
        password = ""
        invalid = False
        
        for c_type in selection:
            characters+= CHARACTER_TYPES[c_type]

        for _ in range(n):
            password += secrets.choice(characters)

        for choice in selection :
            found = False

            for character in CHARACTER_TYPES[choice] :
                if character in password :
                    found = True
                    break

            if not found :
                invalid = True 
                break
            
    return password


def get_valid_length():
    prompt =  "Enter desired length : "
    while True :
        n = input(prompt)
        try:
            n = int(n)
            if (n <= 0 or n>128):
                prompt = "Invalid length. Enter a number between 1 and 128 :"
            else:
                return n
            
        except ValueError:
            prompt = "Invalid length. Enter a number between 1 and 128 :"
            

def get_character_types (prompt = None) :
    if prompt is None:
        prompt = "Enter desired character type(s) (low,up,num,sym) :"
    invalid = True
    while invalid :
        invalid = False 
        choices = input(prompt)
        choices = re.split(r"\W+",choices)
        choices = set(choices)
        choices.discard("")
        
        
        allowed_choices = set(CHARACTER_TYPES)

        invalid_choices = choices - allowed_choices
        if invalid_choices or not choices:
            invalid = True   #outer while loop unecessary. 
            print( "Invalid Character type(s) " ,invalid_choices, "detected.") 
            prompt = "Enter valid character type(s) (low,up,num,sym) : "
                    
    return choices


def get_password_amount () :
    prompt = "How many passwords would you like? "
    while True :
        try:
            n = int(input(prompt))
            if (n<1 or n>100):
                prompt = "Invalid number. Enter a number between 1 and 100 : "
            else:
                return n
        except ValueError:
            prompt = "Invalid number. Enter a number between 1 and 100 :"


def get_pool_size(selection) :
    pool_size = 0
    for choice in selection :
        if choice in CHARACTER_TYPES :
            pool_size += len(CHARACTER_TYPES[choice])
    return pool_size


def get_entropy(length,selection):
    
    valid_password_count = get_pool_size(selection)**length

    for i in range(1,len(selection)+1):
        for excluded in combinations(selection,i):
            valid_password_count += (-1)**i * get_pool_size(selection - set(excluded))**length

    entropy = math.log2(valid_password_count)

    return round(entropy,2)

    

def main() :
    print("Password Generator")
    
    amount = get_password_amount()
    length = get_valid_length()
    selection = get_character_types()
    passwords = []
    
    while length < len(selection):
        prompt = f"Too many character types for a password of length {length}. Try again :"
        selection = get_character_types(prompt)
    
    entropy = get_entropy(length,selection)


    for _ in range(amount):
        password = generate(length,selection)
        passwords.append(password)
        
    print("Generated Password(s) :")
    
    for i ,password in enumerate(passwords,start=1) :
        print(f"{i}. {password}")
    
    print(f"Password entropy : {entropy} bits")


if __name__ == "__main__" :
    main()



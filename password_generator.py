import argparse
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
LIMITS = {
    "min_length" : 1,
    "max_length" : 128,
    "min_amount" : 1,
    "max_amount" : 100
}


def generate_passwords(amount, length, selection): 
    
    characters = ""
    for c_type in selection:
            characters+= CHARACTER_TYPES[c_type]
    
    passwords = []
    
    while len(passwords) < amount :
        password = ""

        for _ in range(length):
            password += secrets.choice(characters)

        if is_valid_password(selection, password):
            passwords.append(password)
            
    return passwords

 
def get_valid_length():
    prompt =  "Enter desired length : "
    
    while True :
        length = input(prompt)
        
        if validate_length(length) :
            return int(length)
        else:
            prompt = f"Invalid length. Enter a number between {LIMITS['min_length']} and {LIMITS['max_length']}:" 


def get_character_types (prompt = None) :
    if prompt is None:
        prompt = f"Enter desired character type(s) {CHARACTER_TYPES.keys()} :"
    
    while True :
        
        choices = input(prompt)
        choices = re.split(r"\W+",choices)
        choices = set(choices)
        choices.discard("")
        
        
        if validate_selection(choices):
            return choices
        else:
            prompt = f"Invalid character type(s) detected. Choose from {CHARACTER_TYPES.keys()} :"

    
def get_password_amount () :
    prompt = "How many passwords would you like? "
    while True :
        n = input(prompt)
        if validate_amount(n):
            return int(n)                                       
        else:
            prompt = f"Invalid number. Enter a number between {LIMITS['min_amount']} and {LIMITS['max_amount']} :"


def get_pool_size(selection) :
    pool_size = 0
    for choice in selection :
        pool_size += len(CHARACTER_TYPES[choice])
        
    return pool_size


def get_entropy(length, selection):
    
    valid_password_count = get_pool_size(selection)**length

    for i in range(1, len(selection) + 1):
        for excluded in combinations(selection,i):
            valid_password_count += (-1)**i * get_pool_size(selection - set(excluded))**length

    entropy = math.log2(valid_password_count)

    return round(entropy, 2)


def get_arguments ():
    
    min_l = LIMITS['min_length']
    max_l = LIMITS['max_length']
    min_a = LIMITS["min_amount"]
    max_a = LIMITS["max_amount"]
    types = ",".join(CHARACTER_TYPES)

    parser = argparse.ArgumentParser(description= "Generate secure passwords")
    parser.add_argument(
        "--length",
        type=int,
        choices=range(min_l, max_l + 1),
        metavar= "LENGTH",
        help= f"Password length ({min_l}-{max_l})")    
    
    parser.add_argument(
        "--amount",
        type= int,
        choices=range(min_a, max_a + 1),
        metavar= "AMOUNT",
        help= f"Amount ({min_a}-{max_a})")
    
    parser.add_argument(
        "--type",
        nargs="+",
        choices=CHARACTER_TYPES,
        metavar= "TYPES",
        help= f"Types : {types}")
    
    args = parser.parse_args()
    return args


def validate_length (length):
    
    try :
        length=int(length)
        if length in range(LIMITS["min_length"],LIMITS["max_length"] + 1):       
            return True
    except (ValueError,TypeError):
        return False 
    return False


def validate_amount(amount):
    try:
        amount = int(amount)
        if amount in range(LIMITS["min_amount"],LIMITS["max_amount"] + 1):               
            return True
    except (ValueError,TypeError):
        return False 
    return False


def validate_selection(selection):
    
    try:
        selection = set(selection)
        allowed_choices = set(CHARACTER_TYPES)
        invalid_choices = selection - allowed_choices
    except TypeError :
        return False
    
    if invalid_choices or not selection:
        return False
    return True 


def is_valid_password(selection, password) :

    omitted_choices = set(CHARACTER_TYPES) - selection

    for choice in selection :
        found = False                 

        for character in CHARACTER_TYPES[choice] :
            if character in password :
                found = True
                break

        if not found :
            return False 

    for omitted in omitted_choices :

        for character in password:
            if character in CHARACTER_TYPES[omitted]:
                return False 

            
    return True


def print_results(passwords,entropy):
    print("Password Generator")
    print("Generated Password(s) :")                        
        
    for i ,password in enumerate(passwords, start=1) :
        print(f"{i}. {password}")

    print(f"Password entropy : {entropy} bits")


def resolve_inputs(args):
    length = args.length 
    selection = set(args.type) if args.type is not None else None
    
    if selection is not None and length is not None :
        if length < len(selection) :
            print (f"Error. Too many character types for a password of length {length}.")
            return False 
    
    elif selection is None and length is not None :
        selection = get_character_types()
        
        while length < len(selection):
            prompt = f"Error. Too many character types for a password of length {length}. Select fewer types :" 
            selection = get_character_types(prompt)
    elif selection is not None and length is None :
        length = get_valid_length() 

        while length < len(selection) :
            prompt = f"Error. Too many character types for a password of length {length}. Enter greater length :"
            length = get_valid_length(prompt)
    else :
        length = get_valid_length()
        selection = get_character_types()

        while length < len(selection) : 
            print(f"Error. Too many character types for a password of length {length}.") 
            print(f"Current length : {length}" )
            print(f"Current selection : {selection}.")
            entry = input("Enter greater length or fewer types :")

            try :
                entry = int(entry)
                length = entry 
            except ValueError:
                selection = re.split(r"\W+",entry) 
                selection = set(selection)
                selection.discard("")
            except TypeError:
                continue 
    result = (length,selection)
    return result
            


def main() :
    
    args = get_arguments()

    if args.amount is None :
        amount = get_password_amount()
    else:
        amount = args.amount


    results = resolve_inputs(args)
    if results is False:
        return

    length, selection = results
    
    
    passwords = generate_passwords(amount,length,selection)
    entropy = get_entropy(length, selection)

    print_results(passwords,entropy)
    
    

if __name__ == "__main__" :
    main()



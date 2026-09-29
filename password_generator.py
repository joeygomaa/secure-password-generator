import secrets
import string
import re
CHARACTER_TYPES = {
    "low": string.ascii_lowercase,
    "up" : string.ascii_uppercase,
    "num" : string.digits,
    "sym" : string.punctuation
}
def generate(n,selection):
    password = ""
    characters = ""
    
    

    for c_type in selection:
        password+=secrets.choice(CHARACTER_TYPES[c_type])
        characters+= CHARACTER_TYPES[c_type]

    for i in range(n-len(selection)):
        password += secrets.choice(characters)
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
        if invalid_choices :
            invalid = True   #outer while loop unecessary. 
            print( "Invalid Character type(s) " ,invalid_choices, "detected.") 
            prompt = "Enter valid character type(s) (low,up,num,sym) : "
                    
    return choices

def fisher_yates_shuffle(password):
    password_list = list(password)
    length = len(password_list)-1
    for i in range(length,0,-1):
        j = secrets.choice(range(0,i+1))
        password_list[j],password_list[i]=password_list[i],password_list[j]
    shuffled_password = "".join(password_list)
    return shuffled_password

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

    
def main() :
    print("Password Generator")
    
    amount = get_password_amount()
    length = get_valid_length()
    selection = get_character_types()
    passwords = []

    while length < len(selection):
        prompt = f"Too many character types for a password of length {length}. Try again :"
        selection = get_character_types(prompt)

    for _ in range(amount):
        password = generate(length,selection)
        password = fisher_yates_shuffle(password)
        passwords.append(password)
        
    print("Generated Password(s) :")
    for i ,password in enumerate(passwords,start=1) :
        print(f"{i}. {password}")

if __name__ == "__main__" :
    main()



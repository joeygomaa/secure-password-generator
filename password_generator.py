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
    prompt =  "Enter a number between 1 and 128 : "
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
        print(choices)
        
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

    
def main() :
    print("Password Generator")
    
        
    length = get_valid_length()
    selection = get_character_types()

    while length < len(selection):
        prompt = "Too many character types for a password of length " + str(length) + ". Try again :"
        selection = get_character_types(prompt)
     
    unshuffled_password=generate(length,selection)
    print("Generated Password : " , fisher_yates_shuffle(unshuffled_password))
    

if __name__ == "__main__" :
    main()



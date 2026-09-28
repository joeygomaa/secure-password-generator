print("Password Generator")
import secrets
import string

def generate(n,low,up,num,sym):
    password = ""
    characters = ""
    count = 0
    if low:
        password+= secrets.choice(string.ascii_lowercase)
        characters+= string.ascii_lowercase
        count+=1
    if up: 
        password+= secrets.choice(string.ascii_uppercase)
        characters+= string.ascii_uppercase
        count+=1
    if num:
        password+= secrets.choice(string.digits)
        characters+= string.digits
        count+=1
    if sym:
        password+= secrets.choice(string.punctuation)
        characters+= string.punctuation
        count+=1
    if n<count:
        print("Error. Too many types for desired password length.")
        return
    for i in range(n-count):
        password += secrets.choice(characters)
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

def get_character_types () :
    prompt = "Please enter the types of characters, that the password should contain (low,up,num,sym) separated by comma :"
    invalid = True
    while invalid :
        invalid = False 
        choices = input(prompt)
        choices = choices.split(",")

        clean_choices = []
        allowed_choices = ["low","up","num","sym"]


        for type in choices :
            type = type.strip()
            clean_choices.append(type)

        for i in clean_choices :
            if i not in allowed_choices :
                prompt = "Invalid type " + i + " detected. Please try again : "
                invalid = True 
                break

        
    low = False
    up = False 
    num = False
    sym = False 

    for type in clean_choices :
        if type == "low":
            low = True 
        elif type == "up" :
            up = True
        elif type == "num" :
            num = True
        elif type == "sym":
            sym = True
    return low,up,num,sym
    

length = get_valid_length()
low,up,num,sym = get_character_types()
generate(length,low,up,num,sym)


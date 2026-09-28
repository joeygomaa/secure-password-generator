import secrets
import string

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

        clean_choices = set()
        allowed_choices = set(CHARACTER_TYPES)


        for character_type in choices :
            character_type = character_type.strip()
            clean_choices.add(character_type)

        invalid_choices = clean_choices - allowed_choices
        if invalid_choices :
            invalid = True 
            print( "Invalid Character type(s) " ,invalid_choices, "detected.") 
            prompt = "Please enter valid character type(s) (low,up,num,sym) : "
                    
    return clean_choices

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
    invalid = True
    while invalid :
        invalid = False
        length = get_valid_length()
        selection = get_character_types()
        if length>= len(selection) :
            unshuffled_password=generate(length,selection)
            print(fisher_yates_shuffle(unshuffled_password))
        else:
            invalid = True
            print("Error. Too many types for desired password length.")

if __name__ == "__main__" :
    main()



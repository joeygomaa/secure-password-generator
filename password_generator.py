print("Password Generator")
import secrets
import string
password = ""
for i in range(12):
    password += secrets.choice(string.ascii_lowercase)
print("Generated password :" , password)
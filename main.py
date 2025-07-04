import secrets
import string

print("Hello Welcome to the Password Generator by SyT")
print("-------------------------------")

length = input("Please enter the length of the password you desire: ")
use_special_chars = input("Do you want to include special characters? (yes/no): ").strip().lower()
use_digits = input("Do you want to include numbers? (yes/no): ").strip().lower()

def passwordGenerator(l, include_special, include_digits):
    characters = string.ascii_letters
    if include_special == "yes":
        characters += string.punctuation
    if include_digits == "yes":
        characters += string.digits

    password = ''.join(secrets.choice(characters) for _ in range(int(l)))
    return password

newpassword = passwordGenerator(length, use_special_chars, use_digits)

print("Password is created: ", newpassword)
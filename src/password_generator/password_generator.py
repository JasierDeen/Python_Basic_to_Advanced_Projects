import string
import secrets

def contains_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False    

def contains_symbols(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length, symbols, upper_case):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if upper_case:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == "__main__":

    print("\n---- PASSWORD GENERATOR ----\n")
    
    no_of_passwords = int(input("How many password/s you need: "))
    password_length = int(input("\nEnter the length of the password/s ? "))
    has_symbols = input("\nDo you want special characters included in your password (y/n) ? ").lower() == "y"
    has_upper_case = input("\nDo you want upper case included in your password (yes/no) ? ").lower() == "y"
    
    print("\nYour password/s: \n")
    for i in range(no_of_passwords):
        new_pass = generate_password(password_length, has_symbols, has_upper_case)
        specs = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
        print(f"{i} --> {new_pass} ({specs})")    


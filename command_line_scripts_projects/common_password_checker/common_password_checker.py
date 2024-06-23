def check_password(password):

    with open('passwords.txt', 'r') as f:
        common_passwords = f.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password.lower() == common_password:
            print(f"{password}: \u274C (Common Password #{i})")
            return
        
    print(f'{password}: \u2705 (Unique Password)')


if __name__ == '__main__':

    print('\n---- Common Password Checker ----\n')
    user_password = input("Enter a password: ")
    while len(user_password)==0:
        user_password = input("You didn't enter anything. Please enter a password: ")
    check_password(user_password)
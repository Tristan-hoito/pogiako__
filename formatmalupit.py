import re

def username_pogi():
    while True:
            username = input("Enter Username: ")
            pattern = r"^[a-zA-Z]+_[0-9]"
            if re.match(pattern, username):
                return username
            else:
                print("")
                print("Invalid Username")
                print("")
                continue
    
def password_gwapo():
    while True:
        password = input("Enter Password: ")
        pattern = r"^[0-9]"
        if re.match(pattern, password) and len(password) >= 8:
            return password
        else:
                print("")
                print("Invalid Password")
                print("")
                continue

def register_account():
    username = username_pogi()
    password = password_gwapo()
    print('')
    print(f"Account Registered \n Username: {username} \n Password: {password}")
    print("")

register_account()
import re

while True: 
        username = input("Enter username: ")
        pattern = r"^[a-zA-Z]+_[0-9]"
        if re.match(pattern, username):
            while True:
                password = input("Enter password: ")
                pattern2 = r"^[0-9]"
                if re.match(pattern2, password) and len(password)>= 8:
                    print("")
                    print("Account Registered")
                    print(f"Your username is {username} and your password is {password}\n and now, everyone knows your password!")
                    print("")

                else:
                    print("Invalid password")
                    break

                break
        else:
            print("Invalid username")
            break



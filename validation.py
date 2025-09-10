import re

while True:
    try:
        age = int(input("Enter age: "))
        
        if 0 <= age <= 120:
            print(f'Your age is {age}')
            break

        else:
            print("Enter a valid age inside the range (0-120): ")
            continue

    except ValueError:
        print("Invalid Input")
    continue

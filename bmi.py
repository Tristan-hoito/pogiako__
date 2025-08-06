#bmi calculator kg and cm
# whiletrue for looping
while True:
    try:
        #input for name, cm and kg
        name = str(input("Enter your name: "))
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))

        if weight <= 0 or height <= 0:     
            print("Invalid input. Height and weight must be positive numbers.")
            continue

        # calculator ng bmi
        bmi = weight / ((height / 100) ** 2)

        #bmi categories
        UNDERWEIGHT = bmi <= 18.5
        HEALTHYWEIGHT = bmi <= 24.9
        OVERWEIGHT = bmi <= 29.9
        OBESITY = bmi >= 30

        #if else statement for picking categories
        if UNDERWEIGHT:
            category = 'Underweight'
        elif HEALTHYWEIGHT:
            category = 'Healthy weight'
        elif OVERWEIGHT:   
            category = 'Overweight'
        elif OBESITY:
            category = 'Obesity'
        else:
            category = 'Invalid BMI'

        #output ng results
        print(f'Hello {name}, your BMI is: {bmi:.2f}, you are {category}!')
        break

    #error handling
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")  
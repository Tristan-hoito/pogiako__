temp_value = float(input("Enter Temperature Number:"))
unit = input('Enter Temperature Unit F/C:').upper()

if unit == 'F':
    result = ((9 / 5) * temp_value) + 32
    funit = '°C'
elif unit == 'C':
    result = (temp_value - 32) * 5 / 9
    funit = '°F'
else:
    result = 'Invalid'
    funit = 'Results'
<<<<<<< HEAD
print(f'Result: {result:.2f} {funit}')
=======
print(f'Result: {result:.2f} {funit}')
>>>>>>> 39b764ca844205cd873672d995f4b97e56e94163

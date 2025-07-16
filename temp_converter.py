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
print(f'Result: {result:.2f} {funit}')

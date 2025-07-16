sub1 = float(input('Enter First Subject Grade:'))
sub2 = float(input('Enter Second Subject Grade:'))
sub3 = float(input('Enter Third Subject Grade:'))

ave = (sub1 + sub2 + sub3) / 3
if 100 >= ave >= 89.5:
    grade = 'A (Excellent)'
elif 89.4 >= ave >= 79.5:
    grade = 'B (Very Good)'
elif 79.4 >= ave >= 69.5:
    grade = 'C (Improvement Needed)'
elif 69.4 >= ave >= 59.5:
    grade = 'D (Close Fail)'
elif 59.4 >= ave >= 0:
    grade = 'F (Fail)'
else:
    grade = 'Invalid'
    
print(f'Result: {ave:.2f} {grade}')
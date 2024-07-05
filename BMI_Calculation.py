def calculate_bmi(height, weight):   
    return weight / (height ** 2)


height = float(input('Please provide your height in meters: '))
weight = float(input('Please provide your weight in kilograms: '))

bmi = calculate_bmi(height, weight)

print(f'Your BMI is: {bmi:.2f}')

# Determine weight category based on BMI
if bmi <= 18.5:
    print('Underweight')
elif 18.5 < bmi <= 25.0:
    print('Normal weight')
else:
    print('Overweight')

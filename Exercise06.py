'''
Exception Handling: 
a. Create a function to use for exception handling.
b. User should input two numbers, say number1 and number2.
c. Create try/except/else block to handle following exceptions.
i. If number1>=200, the function should raise ValueError exception and notify the 
user by printing a message.
ii. If number2<=50, the function should raise ValueError exception and notify the 
user by printing a message.
iii. Number3 is the sum of number1 and number2 and if number3>=300, the 
function should raise ValueError exception and notify the user by printing a 
message. 
iv. The except block should print the message given by the ValueError
v. If no exception is found, function should execute the else block with a printed 
message.
'''
def SumTwoNumbers():
    try:
        num1 = int(input("Please enter number1: "))
        num2 = int(input("Please enter number2: "))
        num3 = num1 + num2

        if num1 >= 200:
            raise ValueError(f"Number1 out of range, you must enter a number less than 200, you entered: {num1}")
        if num2 <= 50:
            raise ValueError(f"Number2 out of range, you must enter a number greater than 50, you entered: {num2}")
        if num3 >= 300:
            raise ValueError(f"Sum between Number1 and Number2 out of range, it must be less than 300, and it is: {num3}")

    except ValueError as e:
        print(e)
        return None
      
    else:
        print(f"No exception found. The sum of number1 and number2 is: {num3}. Thanks")

result = SumTwoNumbers()
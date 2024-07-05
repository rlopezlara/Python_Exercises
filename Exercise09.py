'''
Create a program that converts a decimal number to binary
'''

def integer_binary(integer):
    if integer == 0:
        return "0"
    
    binary = ""
    
    while integer > 0:
        res = integer % 2
        binary = str(res) + binary
        integer = integer // 2
    return binary

print(integer_binary(129))

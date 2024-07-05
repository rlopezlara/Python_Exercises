'''
a)	Use the pip tool to install the pyinputplus module. 
b)	Write a custom validation function that will only allow the user to enter words 
with an even number of letters and that the last letter is a “y” , now write a proof of concept code 
to incorporate and test this function into the inputCustom function.
'''

import pyinputplus as pyip
import re

def evenWordFinalY(word):
    if not word.endswith('y'):
        raise Exception("The word must finish in letter 'y'")
    elif len(word) % 2 != 0:
        raise Exception("The word must have even letters")
    
word = pyip.inputCustom(evenWordFinalY, prompt='Enter a word with an even number of letters that ends with y: ')

print(f"You entered a valid word: {word}")

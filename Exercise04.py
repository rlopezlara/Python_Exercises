'''write a function that will take a single list argument of 
three strings (do not test for this in the function). The purpose of the function is to write the first 
and last character of each string to a text file. Once successfully completed have the function return 
“1” to the caller.
Now write code outside the function that will ask the user for three individual strings using input 
validation through pyinputplus to ensure that the three strings are one of a choice of five using the 
inputMenu function. Once entered convert the three words to a list and pass to the function as an 
argument. Once the function confirms a successful operation to the caller print the following 
message to the user (“File successfully written.”)'''

import pyinputplus as pyip
import os 

def findString(words):
  
  file1= open("C:\\Users\\rdglo\\Desktop\\Rodrigo\\Python Exercises\\Exercise04text.txt", mode ="w")
  for i in words:
    firtLetter = i[0]
    lastLetter = i[-1]
    file1.write(firtLetter + lastLetter)
  return 1    

word1 = pyip.inputMenu(['yellow', 'orange', 'cherry', 'grapes', 'apple'], numbered=True, prompt="Please select the first word: \n")
word2 = pyip.inputMenu(['yellow', 'orange', 'cherry', 'grapes', 'apple'], numbered=True, prompt="Please select the second word: \n")
word3 = pyip.inputMenu(['yellow', 'orange', 'cherry', 'grapes', 'apple'], numbered=True, prompt="Please select the third word: \n")

newlist = [word1, word2, word3]

result = findString(newlist)

if result == 1:
    print("File successfully written. With the word =", newlist)
    

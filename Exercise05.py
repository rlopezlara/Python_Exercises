'''
write a python function which will return a list made up of 10 
random “strings” where each string has a random length from 2,4 or 6, letters and each letter is randomly 
chosen from the alphabet, however the first letter must be ‘a’. Now write the strings to a text file. Write 
python code that will launch the notepad application with a preloaded text file that contains 10 random 
strings, 20 seconds from the moment the python program runs. Once open, instruct the user to manually 
retype the ten words in the notepad application then close the application. Once the application is closed, 
wait for 15 seconds, then tell the user approximately how long it took them to type the ten words.
'''

import os
import random
import datetime, time
import subprocess

file_path = r"C:\Users\rdglo\Desktop\Rodrigo\Python Exercises\Exercise05Text.txt"


def creatingStrings():
    lenght = random.choice([2,4,6])
    letters = 'abcdefghijklmnopqrstuvwxyz'
    randomword = "a"
    
    for k in range(1,lenght):
        randomword += random.choice(letters)            
    return randomword

fileCreate = open(file_path , mode="w")
for k in range(10):
    random_string = creatingStrings()
    fileCreate.write(str(k+1)+ "-" + random_string + '\n')

fileCreate.write("Please, manually write the same words" + '\n')
for i in range(1,11):
    fileCreate.write(str(i)+ "-" + '\n')

fileCreate.close()
print("10 Strings created successfully! Now wait 20 seconds to the file open!")


time.sleep(20)
Opentext = subprocess.Popen(['notepad.exe', file_path])
startTime = time.time()

Opentext.wait()
Opentext.poll()
endTime = time.time()
elapsedTime = round(endTime - startTime,2)
print("Wait 15 seconds to see how much time you spent.")
time.sleep(15)

print("You take " + str(elapsedTime) + " seconds typing 10 additionals words")
print("End")

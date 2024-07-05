#Question 1
'''
Write a function that will take a single string argument.The purpose of the function is to return the first and last letter of the argument as a single string.
For example if the argument passed to the 	function was “ABCDE” , the function would return “AE”.
Now test the function to ensure it works properly.
'''

stringWord = 'HELLO WORLD'
letter1 = stringWord[0]
letter2 = stringWord[-1]

print(f' Answer question 1 word {stringWord} = {letter1},{letter2}')

print("")
print("")
#Question 2
'''
Write a function that will take one string argument of any length, the purpose of the function is to
determine how many times the first two letters of the argument occur in the rest of the argument,
then return that number to the caller. 	For example, if the argument was “ABCDABGHABGYTAB” 	the return 
value would be 3.  Now test the function to ensure it works properly.
'''

StringArg = 'rodrigorodrigorodrigoro'

twoLetters = StringArg[0:2]

count=0
for i in range(len(StringArg)):
    
    if twoLetters == StringArg[i+2:i+4]:
        count +=1

print("Answer question 2, The two first letters occur " + str(count)+ " in the sentance")


stringWord = 'ABCDABGHABGYTAB'



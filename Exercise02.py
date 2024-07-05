'''
Write a function that will take a single list
argument of any length, that contains an even number of words. 
The purpose of the function is to re-arrange the list such that every pair of words is swapped.
For example, if the list was:  	[‘AA’,’BB’,’CC’,DD’,’EE’,’FF’], the new list would be [‘BB’,’AA’,’DD’,CC’,’rodFF’,’EE’],
once completed the 	function will return the list to the caller.
Now test the function by writing a script that will ask the user for a sentence with an even number of words, keep asking until they provide a
sentence with an even number of words.
'''
def swappedList():
    listOne ='g'

    while len(listOne) %2 != 0: #Asking for a even string
        listOne = input(" Please enter a pair of even words sentence: ")
        listOne =listOne.split() #making a list
    print('Original List: ' + str(listOne)) #print the list

    for i in range(0, len(listOne), 2):
        listOne[i], listOne[i + 1] = listOne[i + 1], listOne[i] #changing the position

    print('New List swapped: ' + str(listOne)) #print the new list

swappedList()
 
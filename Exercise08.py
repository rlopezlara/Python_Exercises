'''
Create a function that, given a list of numbers, returns the largest sum of 2 consecutive elements

'''
def pairSum(listone):
    max = 0
    for i in range(len(listone)-1):
        sum = listone[i] + listone[i+1]
        if sum > max:
            max = sum
    return max

print(pairSum([3,4,5,7,1,2,9,12,8,7]))     
    
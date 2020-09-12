# Question 1:
# Write a python Function for finding is a given number prime or not and do Unit Testing on it using PyLint and Unittest Library.

# Using PyLint
'''
Module to check weather the given number is even or odd.
'''
def prime(num):
    '''
    Function which checks out whether the given number is even or odd.
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            return print("It is a Prime Number")
    return print("It is not a Prime Number")
n = int(input("enter the number :"))
prime(n)

# output:
# enter the number :3
# It is a Prime Number

# Using Unittest

'''
file for prime
'''
def primeno(check_number=5):
    '''
    function to check if prime
    '''
    factors_count = 0
    for num in range(1, check_number+1):
        if check_number % num == 0:
            factors_count = factors_count + 1
    if factors_count == 2:
        return True
primeno()

# output:
# True

# ***************************************************************************************************************

# Question 2:
# Make a small generator program for returning armstrong numbers in between 1-1000 in a generator object.

list_1 = list(range(1,1000))

def getArmstrongNumGen(list_1):
    for num in list_1:
        order=len(str(num))
        temp=num
        sum=0
        while temp >0:
            digit=temp%10
            sum=sum+digit**order
            temp=temp//10
        if sum==num:
             yield num

print(list(getArmstrongNumGen(list_1)))

# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

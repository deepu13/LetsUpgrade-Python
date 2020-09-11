# Question 1:
# Write a decorator function for taking input for your any kind of function you want to build.
# For example- You make a fibonacci series function, in which your input range is been defined by the decorator program input

def fibonacci(num):
  fib={}
  def fibo(x):
    if x not in fib:
      fib[x]=num(x)
    return fib[x]
  return fibo

@fibonacci
def fibonum(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonum(n-1)+fibonum(n-2)
  
print(fibonum(14))

# output:
# 377

# **********************************************************************************************************************

# Question 2:
# For this challenge you need to develop a Python program to open a file in read only mode and try writing something to it 
# and handle the subsequent errors using Exception Handling

import sys

try:
  file=open("Day8.txt","r")
  file.write("Assignment for Day 8")
  file.close()
except Exception as e:
  print("Unable to open file")
  print("Error is:",e)
finally:
  print("Example for Exception Handling")

# output:
# Unable to open file
# Error is: [Errno 2] No such file or directory: 'Day8.txt'
# Example for Exception Handling

# **********************************************************************************************************************
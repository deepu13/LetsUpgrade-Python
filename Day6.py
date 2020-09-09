# Question 1:
# For this challenge, create a bank account class that has two attributes:
# Ownername and Balance
# and two methods:
# Deposit and Withdraw
# as an added requirement, withdrawals may not exceed the available balance
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn

class Bank_Account: 
  def __init__(self): 
    self.ownerName = ""
    self.balance=0
    
  def set_ownerName(self):
    name = input("\nEnter the Name: ")
    self.ownerName = name
    
  def get_ownerName(self):
    print("Welcome ",self.ownerName)
    
  def deposit(self): 
    amount=float(input("\nEnter amount to be Deposited: ")) 
    self.balance += amount 
    print("Amount Deposited : ",amount) 
  
  def withdraw(self): 
    amount = float(input("\nEnter amount to be Withdrawn: ")) 
    if self.balance>=amount: 
      self.balance-=amount 
      print("You Withdrew : ", amount)
      print("Thank you! Have a Great Day !")
    else: 
      print("Insufficient balance  ")
      chk_bal = input("\nCheck Available Balance (Y/N): ")
      if chk_bal.lower() == "y":
        print("Net Available Balance : ",self.balance)
        print("Thank you! Have a Great Day !")
      else:
        print("Thank you! Have a Great Day !")


acc = Bank_Account() 
acc.set_ownerName()
acc.get_ownerName()
acc.deposit() 
acc.withdraw()

# output:
# Enter the Name: abc
# Welcome  abc
# Enter amount to be Deposited: 10000
# Amount Deposited :  10000.0
# Enter amount to be Withdrawn: 5000
# You Withdrew :  5000.0
# Thank you! Have a Great Day !

# output:
# Enter the Name: xyz
# Welcome  xyz
# Enter amount to be Deposited: 1000
# Amount Deposited :  1000.0
# Enter amount to be Withdrawn: 5000
# Insufficient balance
# Check Available Balance (Y/N): y
# Net Available Balance :  1000.0
# Thank you! Have a Great Day !

# ********************************************************************************************

# Question 2:
# For this challenge, create a cone class that has two attributes:
# R=Radius and h=Height
# And two methods
# Volume = π r2 * (h/3)
# Surface area : base = π r2, side = π r sqrt(r2+h2)
# Make only one class with functions, as in where required import Math

import math as m
class Cone: 
  def __init__(self): 
    self.radius = 0
    self.height = 0
    self.set_parameters()
    self.calc_Volume()
    self.calc_TSA()
    
  def set_parameters(self):
    radius = float(input("Enter the Radius: "))
    self.radius = radius
    height = float(input("Enter the Height: "))
    self.height = height
        
  def calc_Volume(self):
    r = self.radius
    h = self.height
    volume = m.pi * m.pow(r, 2) * (h/3)
    print("\nVolume : %0.2f"%volume)
        
  def calc_TSA(self):
    r = self.radius
    h = self.height
    base = m.pi * m.pow(r, 2)
    side = m.pi * r * m.sqrt(m.pow(r, 2) + m.pow(h, 2))
    print("\nSurface Areas")
    print("Base  : %0.2f" % base)
    print("Side  : %0.2f" % side)
    print("Total : %0.2f" % (base + side))

shape=Cone()
print(shape)

# output:
# Enter the Radius: 5
# Enter the Height: 2

# Volume : 52.36

# Surface Areas
# Base  : 78.54
# Side  : 84.59
# Total : 163.13

# ********************************************************************************************
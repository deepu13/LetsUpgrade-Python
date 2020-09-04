# Question 1:
# You are all pilots, you want to land a plane safely, so altitude required for landing a plane is 1000ft.
# If it is less than that tell pilot to land the plane
# Or if it is more than that but less than 5000ft ask the pilot to come down to 1000ft
# Else if it is more than 5000ft ask the pilot to go around and try later

altitude = int( input("Enter the altitude \n") )
if(altitude <= 1000):
  print("Land the plane")
elif( altitude > 1000 and altitude < 5000):
  print("Come down to 1000ft")
else:
  print("Go around and try again later!") 

# Example output 1:
# Enter the altitude
# 1000
# Land the plane

# Example output 2:
# Enter the altitude
# 4500
# Come down to 1000ft

# Example output 3:
# Enter the altitude
# 6500
# Go around and try again later!

# ********************************************************************************

# Question 2:
# Print all the prime numbers between 1-200 using for loop and range function

print("The prime numbers between 1 and 200 are")

for i in range(1, 200):
  if(i == 1):
    continue
  flag = 1

  for j in range(2 , i//2 + 1):
    if(i % j == 0):
      flag = 0
      break

  if(flag == 1):
    print(i, end=" ")
  
# output :
# The prime numbers between 1 and 200 are
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
# 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199

# ********************************************************************************
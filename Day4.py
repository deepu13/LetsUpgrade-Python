# Question :
# Print the first Armstrong number in the range of 1042000 to 702648265 
# and exit the loop as soon as you encounter the first Armstrong number.

lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):
  order = len(str(num))
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

  if num == sum:
    print("The first armstrong number is",num)
    break

# output :
# The first armstrong number is 1741725

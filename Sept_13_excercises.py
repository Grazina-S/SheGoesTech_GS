# 1. FizzBuzz 
# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 
# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number
#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    if i % 7 == 0:
        print("Buzz")
    if i % 5 == 0:
        print("Fizz")
    else:
        print(i)
###
#2. Christmas tree 
# Ask user to enter the height of the tree 
# Then Print the tree: Ex. height == 3 
# The printout would be: 
#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

height = float(input("What is the height of your tree?"))
height = round(height)
stars = 1
for i in range(1, height + 1):  
    print(" " * (height - i) + "*" * stars)
    stars  +=2
#
# 3. Primes Check if entered positive number is a prime number.
#  A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?
a = int(input("Please enter a positive round number"))
#NOT FINISHED NEEDS CORRECTIONS
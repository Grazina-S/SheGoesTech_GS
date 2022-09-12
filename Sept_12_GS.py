# 1. Health check
# Ask user for their temperature.
# If the user enters below 35, then output "not too cold"
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever
# remember about type conversion if needed
a = float(input("What is your body temperature?"))
if a < 35:
    print("not too cold")
elif 35 <= a <= 37:
    print("all right")
else:
    print("possible fever")

# 2. Xmas Bonus
# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.
# Task. Ask the user for the amount of the monthly salary and the number of years worked.
# Calculate the bonus.
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)
# b = int(input("What is yout monthly salary?"))
# c = float(input("How long have you been working for this company?"))
# if c > 2:
#     d = (c - 2)*b*0.15
#     print(f"Congrats, you get a bonus of {d} Euros")
# else:
#     print("Sorry no bonus for you")

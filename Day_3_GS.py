# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
username = input("What is your username?")
age = input(f"How old are you {username} ?")
age = int(age)
target_age = 100
age_100 = target_age - age
print(f"So you will be 100 in {age_100} years 😀 ")
import datetime
current_year = datetime.datetime.now().year
age_100_year = current_year + age
print(f"So you will be 100 years old in year {age_100_year}")
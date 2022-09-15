# 1. Confusion
# The user enters a name.
# You print user name in reverse (should begin with capital letter)
# #  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"
# Example:
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?
######
user_name = input("What is your name?")
user_reverese = user_name[ :: -1]
print(f"{user_reverese.capitalize()} , a thorough mess is it not {user_name[0]} ?")

#####
# 2. Almost Hangman
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***


#1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
# PSS function should return the result, not print it.

### MY SOLUTION
def add_mult(a, b, c):
    arg_list = [a, b, c]
    arg_list = sorted(arg_list)
    calc = (arg_list[0] + arg_list[1])*arg_list[-1]
    return calc


testas = add_mult (10, 1, 9)
print(testas)

#### VALDIS SOLUTION
# def add_mult(*args):
#     # number_list = []
#     # for arg in args:
#     #     number_list.append(arg)
#     number_list = list(args) # no need for loop
#     number_list.sort()
#     first_element=number_list[0]
#     second_element=number_list[1]
#     last_element=number_list[-1]
#     # print(first_element, second_element,last_element)
#     calc=(first_element+second_element)*last_element
#     return calc

###################################################
# 2. Palindrome
# Write the function is_palindrome(text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False
# Python has type hints, which are not mandatory but can be used to help the developer
# type hints are like United Nations letters, they are not mandatory but they are useful

def is_palindrome(your_text: str): 
    format_text = your_text.lower().replace(" ", "")
    return format_text == format_text[::-1]
#
testas2 = is_palindrome('Sedek uzu kedes')
print(testas2)
    
# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary
# The parameters of the function are the dictionary d to be processed and the list of values ​​v_list to get rid of.
# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> {'b': 6} because 3 and 5 were in the list of values to delete.
# PS. Remember we can use del d['a'] only if the key 'a' exists.
# !! When resizing a dictionary, we are not allowed to iterate at the same time!

# There are two options: either walk through the copy my_dict.copy.items(), or build a new dictionary. 
# Dictionary comprehension would be one option.
#####               SOLUTION
old_dict = {'a': 5, 'b': 6, 'c': 5, 'd':3, 'e': 7, 'f': 4}
bad_values = [3, 4, 5]

def clean_dict_values(d, v_list):
    new_dict = {}
    for key, value in d.items():
        if value not in v_list:         
             new_dict[key]=value
    return new_dict

###             TEST IF WORKS
clean_dict = clean_dict_values(old_dict, bad_values)
print(clean_dict)
###             YES IT DOES    



# # 1. What's the frequency?
# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 
# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included
#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile

# 
        
# def get_char_count(text):
#     dict = {}
#     for n in text:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(get_char_count('aaabcccc'))
# ##       NOT MY SOLUTION!! 

# # 2. Dictionary editor
# # Write replace_dict_value(d, bad_val, good_val), which returns a dictionary with changed values
# # The parameters of the function are the dictionary d to be processed and the values ​​bad_val to be changed to good_val
# # clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced

# def replace_dict_value(d, bad_val, good_val):
#     print(d)
#     for key, value in d.items():
#         if value == bad_val:
#             d[key] = good_val # so this is the version where we modify the original IN PLACE
#     print(d)
#     return d # returns the original dictionaly

# my_dict = {'a': 5, 'b': 6, 'c': 5}
# print(my_dict)
# new_dict = replace_dict_value(my_dict, 5, 12)
# print(new_dict)
# print(my_dict)
# print("dictionaries are the same dictionary in fact", my_dict is new_dict)  
# # NOT MY SOLUTION AS WELL

# # # 3. Dictionary cleaner
# # 3a. Write clean_dict_value(d, bad_val), which returns a cleaned dictionary without any keys with the value bad_val
# # The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.
# # Example:
# # clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.
# # OUT OF PLACE function, it returns a new dictionary, old one is not changed
# def clean_dict_value(d, bad_val):
#     new_dict = {}
#     for key, value in d.items():
#         if value != bad_val:
#             new_dict[key] = value
#     return new_dict

# print(clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5)) 

# my_dict = {'a': 5, 'b': 6, 'c': 5, 'd':3, 'e': 5, 'f': 5, 'g':8}	
# new_dict = clean_dict_value(my_dict, 5)
# print(new_dict)
# print(my_dict)

# # you can also use dictionary comprehension, STILL OUT OF PLACE
# def clean_dict_value_2(d, bad_val):
#     return {key: value for key, value in d.items() if value != bad_val}

# also_new_dict = clean_dict_value_2(my_dict, 5)
# print(also_new_dict)
# print(my_dict)

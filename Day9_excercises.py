# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.




from statistics import mean


def get_min_avg_max(numbers):
    mini = min(numbers)
    amean = mean(numbers)
    maxi = max(numbers)
    return mini, amean, maxi

##      TEST
randomnumbers = 6, 1, 20, 3
print(get_min_avg_max(randomnumbers))
print(get_min_avg_max ([0,10,1,9]))
###     seems like it's working

# 2. Common Elements

# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements(seq1, seq2, seq3)
# Example:
# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
# 2. b For those with some experience 
# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    return  tuple(set1 & set2 & set3)
    
    #       TEST

result = get_common_elements("abc", ['a', 'b'], ('b', 'c'))
print(result)
## Works
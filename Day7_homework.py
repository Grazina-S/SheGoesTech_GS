# # 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, target_p) that returns the years (full) when target_p is reached.
# If target_p cannot be reached, then we return -1
# Example:
# get_city_year(1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 after the 1st year
# notice that we have an integer (whole number) percentage, so the population after the 1st year is 1070, not 1070.4 or 1070.6

# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year

# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year 

# so the function here returns 3 and is done
# PS. Note that we give perc as a percentage to be converted to a decimal number.
# More test examples:
# get_city_year(1000, 2, -50, 5000) -> -1 
# get_city_year(1500, 5, 100, 5000) -> 15
# get_city_year(1500000, 2.5, 10000, 2,000,000) -> 10
# the trickiest case is something like this
# get_city_year(1000, -3, 50, 2000) -> -1 is the correct answer but how to get there?

#############
def big_city_when (p0, perc, delta, target_p): 
    no_of_years = 0
    while p0 < target_p:
        pop_growth = round(p0*perc/100 + delta)
        if pop_growth > 0:
            p0 += pop_growth
            no_of_years += 1
        else:
            no_of_years = -1
            break
    return no_of_years

##### TEST IF WORKS
years = big_city_when(1000, -3, 50, 2000)
years2 = big_city_when(1500, 5, 100, 5000)  
print(years, years2)
#### YES IT DOES :-)        
# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 

t1 = "aabcf"
t2 = "fab"
t3 = "boo"
planet6 = "Saturn"
planet7 = "Uranus"
planet8 = "Neptune"

def compare_strings (text1, text2, text3):
    good_string = set(text1.lower()) & set(text2.lower())
    bad_string = set(text3.lower())
    return "".join(sorted(good_string - bad_string))

print(compare_strings(t1, t2, t3), compare_strings(planet6, planet7, planet8))

####    ANOTHER WAY, SHORT AND WORKS BUT MESSY TO READ 
def compare_strings_v2 (text1, text2, text3):   
    return "".join(sorted(set(text1.lower()) & set(text2.lower()) - set(text3.lower())))
    
print(compare_strings_v2(t1, t2, t3), compare_strings_v2(planet6, planet7, planet8)) 

##### SOLUTION WITH LOOP

def compare_strings_v3 (text1, text2, text3):
    text1 = text1.lower()
    text2 = text2.lower()
    text3 = text3.lower()
    result =""        
    for c in text1:
        if c in text2  and c not in text3 and c not in result:
            result += c     
    return "".join(sorted(result))
print(compare_strings_v3(t1, t2, t3), compare_strings_v3(planet6, planet7, planet8)) 

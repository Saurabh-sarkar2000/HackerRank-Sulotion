  
import re

def is_float_number(s):
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, s))

test_cases = int(input())

for _ in range(test_cases):
    number = input()
    print(is_float_number(number))
    
    
    
    
    
    
    
    
    
# 1. We import the `re` module to work with regular expressions.
# 2. We define a function `is_float_number(s)` that takes a string 's' as input and checks if it matches the pattern of a valid floating-point number.
# 3. The regular expression pattern `r'^[-+]?[0-9]*\.[0-
#    9]+$" is used to define the valid format for a float number:
#    asserts the start of the string.
#    `[-+]?` matches an optional plus or minus sign at the start.
#    `[0-9]** matches zero or more digits.
#     • '\. matches the decimal point.
#     `[0-9]+' matches one or more digits after the decimal point.
#     • $ asserts the end of the string.
# 4. The function `re.match(pattern, s)`attempts to match the pattern to the input string `s`. 
# If there's a match, it returns a match object, which evaluates to 'True' when converted to a boolean. Otherwise,    
# In this code, I added the strip() method to remove leading and trailing whitespace from the input string. 
# This ensures that any leading or trailing spaces in the input do not affect the validation of the floating-point number.    
    

  
  

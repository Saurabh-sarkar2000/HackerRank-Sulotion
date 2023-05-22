
  
  
  
import re

def is_float_number(s):
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, s))

test_cases = int(input())

for _ in range(test_cases):
    number = input()
    print(is_float_number(number))

  
  

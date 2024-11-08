#capture all numbers in a string

import re

def find_numbers(pattern,input_str):
    return re.findall(input_str,pattern)

print("Enter an input string:")
pattern = input()
test_pattern = '\d+'
print(re.findall(test_pattern,pattern))
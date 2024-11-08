#capture all words in a string that starts with s

import re

def find_numbers(pattern,input_str):
    return re.findall(pattern,input_str,re.IGNORECASE)

input_str = 'She sells sea shells in the sea shore'
test_pattern = r'\bs\w*'
print(find_numbers(test_pattern,input_str))
import re
pattern = 'hello 12 hi 89.Howdy 34'
test_pattern = '\d+'
result = re.findall(test_pattern,pattern)
print(result)
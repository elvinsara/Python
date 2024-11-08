import re
pattern = "^a...s$"
test_pattern="abyss"
if(re.match(pattern,test_pattern)):
    print("matching")
else:
    print("Not matching")
print(re.match(pattern,test_pattern))

#match returnss an Match object ow None
#^ and $ are metacharacters
#[] set of characters that you wish to match
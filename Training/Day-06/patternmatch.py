import re
pattern = '[^1234]'
test_pattern = 'hello'
pattern2 = '1..Rs'
test_pattern2 = '105Rs'
if(re.match(pattern2,test_pattern2)):
    print("matched")
else:
    print("not matched")
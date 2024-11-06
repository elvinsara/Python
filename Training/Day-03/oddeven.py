def odd_or_even(num):
    if num%2==0:
        return "Even"
    return "Odd"

print("Enter a number to check odd or even : ")
num = int(input())
print(odd_or_even(num))
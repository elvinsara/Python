def sum(num1,num2):
    return num1+num2

def difference(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 !=0:
        return num1/num2
def take_input():
    print("Enter num1")
    num1 = int(input())
    print("Enter num2")
    num2 = int(input())
    return num1,num2

choice = 0
while(choice!=5):
    print("----Choose the operation that you want to perform----")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    print("Input your choice")
    choice = int(input())
    
    if(choice==1):
        num1,num2 = take_input()
        print("Sum is "+sum(num1,num2))
    if(choice==2):
        num1,num2 = take_input()
        print("Difference is "+difference(num1,num2))
    if(choice==3):
        num1,num2 = take_input()
        print("Multiplication is "+multiply(num1,num2))
    if(choice==4):
        num1,num2 = take_input()
        print("Division is "+divide(num1,num2))
    if(choice!=5):
        print("Enter a valid choice")

print("Exit")
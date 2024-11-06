def print_name(name,number_of_times):
    for i in range(number_of_times):
        print(name)


print("Enter a name:")
name = input()
print("Enter number of times : ")
number_of_times = int(input())
print("--Printing name--")
print_name(name,number_of_times)
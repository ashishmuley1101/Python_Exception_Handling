
# Catching Specific Exceptions using multiple except block

# The try...except...except block is used to handle exceptions in Python
# Syntax : try:
#               code that may cause exception
#          except exception_name1:
#               code to run when exception_name1 occurs
#          except exception_name2:
#               code to run when exception_name2 occurs

try:
    numerator = int(input("Enter the numerator : "))
    denominator = int(input("Enter the denominator : "))
    result = numerator / denominator
    print(result)

    list = [1, 2, 3, 4, 5]
    index = int(input("Enter the index num : "))
    print(list[index])

except ZeroDivisionError:
    print("Denominator cannot be zero 0.")

except IndexError:
    print("Invalid index number enter try again.")
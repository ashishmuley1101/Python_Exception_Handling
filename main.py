
# Python try with else clause

# else keyword to define a block of code to be executed if no errors were raised.
# Syntax : try:
#               code that may cause exception
#          except exception_name1:
#               code to run when exception_name1 occurs
#          else:
#               code to run else block

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

else:
    sum = sum(list)
    print("Sum of list number : ", sum)

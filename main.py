
# Python try...except...finally block

# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.

# Syntax : try:
#               code that may cause exception
#          except exception_name1:
#               code to run when exception_name1 occurs
#          finally:
#               code run executed no matter whether there is an exception or not.

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

finally:
    print("This is finally block.")

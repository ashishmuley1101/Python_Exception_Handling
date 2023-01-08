
# Python Exception Handling using try and except block

# The try...except block is used to handle exceptions in Python
# Syntax : try:
#               code that may cause exception
#          except:
#               code to run when exception occurs

try:
    numerator = int(input("Enter the numerator : "))
    denominator = int(input("Enter the denominator : "))
    result = numerator / denominator
    print(result)

except:
    print("Denominator cannot be zero 0 ")
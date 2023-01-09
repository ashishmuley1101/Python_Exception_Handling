
# Python User-Defined Exception(Custom Exceptions)

# In Python, we can define custom exceptions by creating a new class that is derived from
# the built-in Exception class.

# Syntax : class CustomError(Exception):
#               ...
#               pass
#
#           try:
#               ...
#
#           except CustomError:
#                 ...

class InvalidAgeException(Exception):  # define Python user-defined exceptions
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a age for voting : "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Voting.")

except InvalidAgeException:
    print("Exception occurred: Enter Invalid Age")

finally:
    print("This is finally block.")

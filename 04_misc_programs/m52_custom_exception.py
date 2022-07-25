# Define a custom exception class which takes a string message as attribute.
class CustomException(Exception):
    def __init__(self, message):
        self.message = message


number = int(input("Enter a number of your choice: "))

try:
    if number < 10:
        raise CustomException("Input is less than 10")
    elif number > 10:
        raise CustomException("Input is greater than 10")
    else:
        raise CustomException("Input is equal to 10")
except CustomException as ce:
    print("Error raised is >> ", ce.message)
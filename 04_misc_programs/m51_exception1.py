# Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide(a, b):
    print(a / b)


try:
    divide(5, 0)
except ZeroDivisionError as ze:
    print("Why are you dividing a number by zero")
    print(ze)
except:
    print("Any other exception")

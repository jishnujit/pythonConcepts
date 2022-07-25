
def divide(dividend, divisor):
    '''
    > When there are no grades in the list, len(grades) will be 0. Here we raise ZeroDivisionError when the divisor = 0.
    This will through the message passed to the exception and it also prints out the traceback lines.
    Now if we do not want this traceback, then we need to put the line in try except block as seen below. This will not
    throw any error instead it throws user friendly message what we give in except block, i.e. skips the try block
    stmt and executes the except block statements
    > Now to get the exception error message we can use modify the code as below
      except ZeroDivisionError as e:
          print(e)
          print("There are no grades in your list")
    :param dividend: sum(grades)
    :param divisor: len(grades)
    :return:
    > if you want to run a particular code only if the try block succeeds then we can put the code under 'else' as
      seen in below code
    > If you need some code to run regardless if the exception is thrown or not, put it under 'finally'
    > Multiple except clauses are possible
    '''
    if divisor == 0:
        raise ZeroDivisionError("Division by ZERO is not possible")

    return dividend / divisor


grades = []
print("Welcome to average grades program")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades in your list")
else:
    print(f"Average grade is {average}.")
finally:
    print("ThankYou")

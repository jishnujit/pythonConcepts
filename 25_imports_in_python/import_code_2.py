'''
> if you run the below code it prints "import_code_2.py:  __main__". Here dunder name should be dunder main as we see
  in the result printed, i.e. every stand alone file you run is considered as dunder main
> __name__ is a global variable in python that changes depending on which file you are in. Allows to differentiate
  between the file you run and a file you import
'''

def divide(divident, divisor):
    return divident / divisor


print("import_code_2.py: ", __name__)
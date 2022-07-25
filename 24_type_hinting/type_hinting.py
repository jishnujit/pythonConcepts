'''
> from python 3.5+
> the below code gives you an error because we cannot find sum of an integer. It needs to be a list. But while writing
  code it is not throwing any error. But when compiling the code it gives error. Why is it so?
> To overcome this we have type hinting, i.e. in the method, we specify near the argument that we are expecting a list
  and the return statement should be float using ->. Eg: def list_avg(sequence: List) -> float:
'''


def list_avg(sequence):
    return sum(sequence)/len(sequence)


list_avg(123)
print("===========================================================================================================")


from typing import List  # import statement should be at top of the file. this is used here only for demonstration


def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)


list_avg(123)
'''
> couple of ways you can import - 1) from file import method/class (from import_code_2 import divide)
  2) import file (import import_code_2) and when calling the function inside this file use file.function name
  e.g. import import_code_2         import_code_2.divide can be used when using the function
> Here when we run import_code_1.py, and when compiler sees import stmt, i.e."from import_code_2 import divide" statment
  compiler stops running "import_code_1.py" and jumps to "import_code_2.py" and run it. It there is another import
  statement in "import_code_2.py", the compiler stops running this file and goes to that imported file and runs it
'''

from import_code_2 import divide

print(divide(10,2))
print("import_code_1: ",{__name__})
'''
prints output as below
import_code_2.py:  import_code_2
5.0
import_code_1:  {'__main__'}
> Now we can see that import_code_2 is not a __main__ thats because it is now imported and used in another class. Here 
  the main would be import_code_1
> So how does python know from where to import. It looks for the path displayed while printing (print(sys.path))
> importing a file from a folder usually requires a dunder init.py file inside that folder
'''
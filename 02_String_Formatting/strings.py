# example 1 - here there is no way of updating the name
name = "Bob"
greeting = "Hello, Bob!"
print (greeting)
name = "Zia"
print (greeting)
#===========================================================================
#2 dynamic updates with format options
name = "bob"
greeting = "Hello, {}! Today is {}"
with_name_format = greeting.format(name,"Monday")
print(with_name_format)
name = "zia"
print(with_name_format) #here the name does not get updated to 'Zia' because the formated string is formed before
# declaring the name as zia. So the interpreter wont consider the change





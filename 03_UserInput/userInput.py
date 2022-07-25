'''
user input always gives a string. so when getting an integer or float we need to type cast it to the reqd type.
If not it throws type error
'''
name = input("Enter your name: ")
print("Hi ",name)


#pgm to convert sq feet to sq meter
sq_feet = int(input("Enter Square feet to conert: "))
sq_meter = sq_feet/10.764
print("{} square feet is {} square meters".format(sq_feet,sq_meter))
print(f"{sq_feet} square feet is {round(sq_meter,2)} square meters")
print(f"{sq_feet} square feet is {sq_meter:.3f} square meters")

'''
Lists
> always enclosed in square brackets []
> you can put different values as long as it is separated by a comma
> can contain combination of string or integer values
> adding and removing element from list possible, i.e. mutable
> They keep the order of elements in lists. Prints it based on the order, can use subscript notation to print l[0]
  print 0th element of list
Tuples
> defined with normal brackets ()
> you can put different values as long as it is separated by a comma
> can contain combination of string or integer values
> adding and removing element from list not possible, i.e. immutable
> They keep the order of elements in lists. Prints it based on the order
> They keep the order of elements in lists. Prints it based on the order, can use subscript notation to print l[0]
  print 0th element of tuples
Set
> defined with curly brackets {}
> you can put different values as long as it is separated by a comma
> can contain combination of string or integer values
> adding and removing element from list possible, i.e. mutable
> cannot have duplicate element in set
> They do not keep the order of elements in lists. Prints it random
'''
list1 = ["Bob", "Rolf", "Anne"]
list2 = [1,2,3,4,5,6,7,8,9,10]
list3 = ["book",10,"light",20]
print("printing list with mixed types", list3)
print("printing list element at 0th index", list1[0])
list1[0] = "Angelina"
print("list1 updated 1st value", list1)
list1.append("Iryn")
print("list1 append: ",list1)

tuple1 = ("Bob", "Rolf", "Anne")
tuple2 = (1,2,3,4,5,6,7,8,9,10)
tuple3 = ("book",10,"light",20)
print("printing tuples with mixed types", tuple3)
print("printing tuple element at 0th index",tuple1[0])

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
set3 = {"book",10,"light",20}
print(set3)
my_tuple = 5,
print("tuple with a single value", my_tuple)

local_friends = friends.difference(abroad) #removes elements of friends from which is in abroad
print("difference of sets: ",local_friends)
unionset = friends.union(abroad)
print("union of sets: ", unionset) #no duplicates allowed in a set
intersectionset = friends.intersection(abroad)
print("intersection: ", intersectionset)


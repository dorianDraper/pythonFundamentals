"""
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets ()
"""
thistuple = ("apple", "banana", "cherry")
print (thistuple)
"""
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item 
has index [1] etc.
>ordered means that the items have a defined order, and that order will not change
>unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
>Since tuple are indexed, tuples can have items with the same value:
"""
print (len(thistuple))
print (type(thistuple))
"""
To create a tuple with only one item, we have to add a comma after the item, 
otherwise Python will not recognize it as a tuple. See below:
"""
tuple_singleitemNok = ("apple")
print (tuple_singleitemNok)
print (type(tuple_singleitemNok))
tuple_singleitemOk = ("apple",)
print (tuple_singleitemOk)
print (type(tuple_singleitemOk))
"""
Tuple items can be of any data type
A tuple can contain different data types
We can build tuples with tuple constructor
"""
thistuple = tuple(("new", "tuple", "constructor", "more and more", "items", "included?"))
print (thistuple)
#We can access tuple items by referring to the index number, inside square brackets:
print (thistuple[1])
"""
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.
"""
print (thistuple[-1])
"""
We can specify a range of indexes by specifying where to start and where to end 
the range. When specifying a range, the return value will be a new tuple 
with the specified items.
"""
print (thistuple[2:5])	#search starts at index 2 (included), end at index 5 (not included).
#By leaving out the start value, the range will start at the first item
print (thistuple[:4])	#from beginning without "items"
#By leaving out the end value, the range will go on to the end of the list
print (thistuple[2:])	#from "constructor" until end
#negative indexes
print (thistuple[-4:-1])
#check if item exists in tuple
if "new" in thistuple:
	print ("Yes 'new' is in the list!")

print ()

"""
Tuples are unchangeable, immutable, meaning that we cannot change, add, or remove 
items once the tuple is created. But there are some workarounds.
We can convert the tuple into a list, change the list, and convert the 
list back into a tuple.
"""
x = ("Nestle", "Cocacola", "Pepsi")
print (x)
print (type(x))
y = list(x)
print (y)
print (type(y))
y[1] = "Fanta"
print (y)
print (type(y))
x = tuple(y)
print (x)
print (type(x))

print ()
"""
New items cannot be added but we can convert into a list, add the items and 
convert the list back into a tuple, same as before
"""
z = ("SOC", "ADI", "MSE", "ITP")
print (z)
print (type(z))
w = list(z)
print (w)
print (type(w))
w.append("w360")
print (w)
print (type(w))
z = tuple(w)
print (z)
print (type(z))
#Items cannot be removed, we can apply same workaround with remove()
#Also we can delete all items by using del()

print ()

"""
When we create tuples we assign values to it=packing. We can also extract the 
values back into variables=unpacking
"""
girls = ("Raquel", "Kenzy", "Arushi")
print (girls)
(cool, hot, exotic) = girls		#number values must match number of variables
print (cool)
print (hot)
print (exotic)

"""
If the number of variables is less than the number of values, we can add an * to 
the variable name and the values will be assigned to the variable as a list:
"""

girls = ("Raquel", "Kenzy", "Arushi", "Mane", "Nallely")
(cool, hot, *exotic) = girls
print (cool)
print (hot)
print (exotic)

#3 options to loop through the values of a tuple==== 
#first by using the for loop:
for x in girls:
	print (x)
"""
second by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
print ()

for i in range(len(girls)):
	print (girls[i])

"""
third by using a while loop. Use the len() function to determine the length of 
the tuple, then start at 0 and loop your way through the tuple items by 
refering to their indexes.
Remember to increase the index by 1 after each iteration.
"""
print ()
i = 0
while i < len(girls):
	print (girls[i])
	i+=1

print ()

#To join two or more tuples we can use the + operator:	====
guys = ("Sinatra", "Brando", "Elvis")
dolls = ("Doris", "Laura", "Melinda")
guysDolls = guys + dolls
print (guysDolls)
guysDolls1 = guysDolls * 2		#we use operator * to multiply tuple's content
print (guysDolls1)
"""
Tuple Methods:
count() = returns number of times a specified value occurs in a tuple
index() = searches tuple for specified value and returs its position
"""
print (count())











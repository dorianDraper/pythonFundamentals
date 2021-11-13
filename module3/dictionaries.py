"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is unordered, changeable and does not allow duplicates.
Dictionaries are written with curly brackets {}, and have keys and values:
"""

thisdict = {
	"brand": "Mini",
	"model": "JCW",
	"year": 2014
}

print (thisdict)
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print (thisdict["brand"])
#Unordered=items does not have a defined order, you cannot refer to an item by using an index.
#Changeable=we can change, add or remove items after the dictionary has been created.
#DuplicatesNotAllowed=Dictionaries cannot have two items with the same key:
thisdict = {
	"brand": "Mini",
	"model": "JCW",
	"year": 2014,
	"year": 2020	#Duplicate values will overwrite existing values:
}
print (thisdict)
print (len(thisdict))	#determine how many items a dictionary has, use the len() function:
#String, int, boolean, and list data types in dictionaries
thisdict = {
	"brand": "Mini",
	"model": "JCW",
	"year": 2014,
	"year": 2020,
	"Electric": False	
}
print (thisdict)
print (type(thisdict))
#ACCESS items by referring to its key name inside square brackets []
print (thisdict["model"])
x = thisdict.get("year")	#method called get() that will give us the same result
print (x)

x = thisdict.keys()	#keys() method will return a list of all the keys in the dictionary.
print (x)
print ()
"""
The list of the keys is a view of the dictionary, meaning that any changes done 
to the dictionary will be reflected in the keys list.
"""
car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": "1964"
}
print (car)
y = car.keys()

car["color"] = "black"
print (car)
print (y)

z = car.values()	#values() method will return a list of all the values in the dictionary.
print (z)
"""
The list of values is a view of the dictionary, meaning that any changes done 
to the dictionary will be reflected in values list.
"""
car["year"] = 2020
print (car)	#keys list gets updated as well:
print (z)
#GET items by using items() method will return each item in dictionary as tuples in a list
w = car.items()
print (w)
#any changes done to the dictionary will be reflected in the items list.
car["Electric?"] = False
print (w)

print ()

#CHECK IF key exists by using the in keyword

if "model" in car:
	print ("Exactly, 'model' is one of the keys in this dictionary")


#CHANGE items=we can change value of specific item by referring to its key name

print ()

car["color"] = "Pink"	#change the item "color"
print (car)

#UPDATE items from the given argument, it must be dictionary or iterable object key:values pairs

car.update({"year": 1999})	#update the item "year" by using update()
print (car)

#ADD items by using a new index key and assigning a value to it

car["motorCV"] = 211
print (car)

#REMOVE items by using pop() method with specified key name

car.pop("model")
print (car)

car.popitem()	#popitem() method removes last inserted item "motorCV"
print (car)

del car["year"]	#del() method removes item with specified key name
print (car)		#del() can also delete dictionary completely, will cause error cause no longer exists

car.clear()		#clear() empties dictionary 
print (car)

"""
LOOP=loop through a dictionary by using a for loop.
the return value are the keys of the dictionary, but there are methods to return the values as well.
"""

print ()

myday = {
	"morning": "master",
	"midday": "Python",
	"lunch": "salad",
	"afternoon": "master2"
}

for x in myday:		#returns all key names one by one
	print (x)

for x in myday.keys():	#also returns all key names one by one
	print (x)

print()

for x in myday:		#returns all values one by one
	print (myday[x])

for x in myday.values():	#also returns all values one by one
	print (x)

print ()

for x, y in myday.items():	#items() mehtod loops through keys and values
	print (x, y)

"""
COPY dictionaries=we cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will 
only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""

print ()

myday2 = {
	"morning": "rest",
	"midday": "work",
	"lunch": "fish",
	"afternoon": "morework"
}

myday2 = myday.copy()
print (myday2)

myday3 = {
	"wow": "rest",
	"youuuu": "work",
	"alsoooo": "fish",
	"hahahaha": "morework"
}

print (myday3)
myday3 = dict(myday2)	#the function dict() also makes a copy
print (myday3)

#NESTED dictionaries=dictionary that contains dictionaries

print ()

myfamily = {
	"child" : {
	"name": "Tobias",
	"year": 2004
	},
	"child1" : {
	"name": "Linus",
	"year": 2003
	},
	"child2" : {
	"name": "Emil",
	"year": 2006
	}
}

print (myfamily)

#DICTIONARY METHODS====
"""
Method 				 	Description
clear()				 	Removes all the elements from the dictionary
copy()				 	Returns a copy of the dictionary
fromkeys()			 	Returns a dictionary with the specified keys and value
get()				 	Returns the value of the specified key
items()				 	Returns a list containing a tuple for each key value pair
keys()				 	Returns a list containing the dictionary's keys
pop()				 	Removes the element with the specified key
popitem()			 	Removes the last inserted key-value pair
setdefault()			Returns the value of the specified key. If the key does not exist: insert the key, 
						with the specified value
update()				Updates the dictionary with the specified key-value pairs
values()			 	Returns a list of all the values in the dictionar
"""

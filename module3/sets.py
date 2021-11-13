"""
Sets are used to store multiple items in a single variable
Sets are one of 4 built-in data types
Sets are collection unordered and unindexed, and do not allow duplicate values
Sets are written with curly brackets {}
"""
thisset = {"My", "First", "Set"}	
print (thisset)
#unordered: have no defined order so we cannot be sure order items will appear
#unchangeable: we cannot change the items after set has been created, but we can add new ones
#duplicates not allowed: we cannot have two items same value
thisset = {"My", "First", "Set", "Set"}	#duplicates are ignored
print (thisset)
print (len(thisset))
#Sets can be of any data type
thisset1 = {False, "one set", "my set", 23}
print (thisset1)
print (type(thisset1))
#we can use set() constructor to make a set
thisset2 = set(("Raquel", "Sheila", "Nuria"))
print (thisset2)

print ()

"""
We cannot ACCESS set items by referring to an index or key, but we can
loop through the set items using for loop or ask if a specified value is 
present in a set by using in keyword
"""
for x in thisset1:
	print (x)

print ()

if "Sheila" in thisset2:
	print ("Sheila is present in thisset2")

#once set is created we cannot CHANGE its items but can add new items with add() method
thisset2.add("Angelina")
print (thisset2)

#to add items from another set into the current set we use update() method
thisset2.update(thisset)
print (thisset2)
#the object in update() method can be any iterable object (tuple, list, dictionaries)
thislist = ["hey", "babe", "sup"]
thisset2.update(thislist)
print (thisset2)

#to REMOVE an item in a set we use the remove() or discard() method
thisset2.remove("Sheila")
print (thisset2)
thisset2.discard("Raquel")
print (thisset2)
#we can also use the pop() method but will remove last item so we will not know what item gets removed as sets are unordered
print ()
x = thisset2.pop()	#we create a variable x and check every time which item we remove
print (x)
print (thisset2)

#the clear() method empties the set
thisset2.clear()
print (thisset2)
"""newset = {"how", "to", "delete"}
del newset
print (newset)
"""
#we can LOOP through the set items by using for loop
for x in thisset1:
	print (x)

"""
JOIN Sets====
There are several ways to join two or more sets in Python.

We can use the union() method that returns a new set containing all items from both sets, 
or the update() method that inserts all the items from one set into another:
Both union() and update() will exclude any duplicate items.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)	#The union() method returns a new set with all items from both sets:
print (set3)

print ()

set1.update(set2)	#The update() method inserts the items in set2 into set1:
print (set1)
#to KEEP ONLY DUPLICATES we use the intersection.update() method that keeps only items present both sets
x = {"smoked", "Converse", "canvas", "Chuck"}
y = {"smoked", "Italy", "Fuck", "canvas"}
x.intersection_update(y)
print (x)

z = x.intersection(y)	#intersection() method will return a new set, that only contains items present in both sets.
print (z)
#KEEP ALL BUT NOT DUPLICATES by using symmetric_difference_update() method only keeps elements not present in both sets.
x.symmetric_difference_update(y)
print (x)
x.symmetric_difference(y)	#will return a new set, that contains only the elements that are NOT present in both sets.
print (x)

#SET Methods====
"""Method 									Description
add()							 	Adds an element to the set
clear()							 	Removes all the elements from the set
copy()							 	Returns a copy of the set
difference()					 	Returns a set containing the difference between two or more sets
difference_update()					Removes the items in this set that are also included in another, specified set
discard()							Remove the specified item
intersection()					 	Returns a set, that is the intersection of two other sets
intersection_update()			 	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()					 	Returns whether two sets have a intersection or not
issubset()						 	Returns whether another set contains this set or not
issuperset()					 	Returns whether this set contains another set or not
pop()								Removes an element from the set
remove()						 	Removes the specified element
symmetric_difference()			 	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	 	inserts the symmetric differences from this set and another
union()								Return a set containing the union of sets
update()							Update the set with the union of this set and others
"""
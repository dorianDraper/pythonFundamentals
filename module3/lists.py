"""
==Python Lists
Lists are used to store multiple items in a sinble variable
Data types to store collections of data are Lists, Tuple, Set, and Dictionary (Arrays)
	List: Collection ordered, changeable, allow duplicates
	Tuple: ordered, unchangeable, allow duplicates
	Set: unordered and unindexed, no duplicates
	Dictionary: unordered, changeable, no duplicates
Lists use square brackets []
"""
thislist = ["apple", "banana", "cherry"]
print (thislist)
"""
List items are ordered, changeable, and allow duplicate values
List items are indexed: first [0] and the second [1]
>>Ordered: items have defined order, that order does not change. If add new item this 
will be placed at the end of the list
>>Changeable: we can change, add or remove items after being created
>>Allow duplicates: List can have items with same value
"""
thislist = ["apple", "banana", "cherry", "banana"]
print (thislist)
print (len(thislist))	#to determine how many items a List has
#List items can be of any data type: str, int, boolean
#List can contain different data types
thislist = ["apple", "banana", "cherry", 1, 22, True]
print (thislist)
print (type(thislist))
# We can use the list() constructor wen creating a new list
newlist = list(("Mini", "BMW", 22, False, "Barcelona"))
print (newlist)

print ()

#Access List Items by referring to the index number
print (thislist[4])
#negative indexing means start from the end: -1 refers to last item, -2 second last item
print (newlist[-2])
#Range of Indexes: we can specify range by specifying where to start and to finish
newlist = list(("Mini", "BMW", 22, False, "Barcelona", "Palmas", True))
print (newlist[1:4])	#starts in "BMW" and ends at 4 ("Barcelona" not included)
print (newlist[1: ])	#leaving out end value, range goes to end of list
print (newlist[-5:-2])	#negative starts from "22" to but not included "Palmas"

if "BMW" in newlist:
	print ("Yes, 'BMW' is in the list")	#check if item in list with in keyword
#to change value of item, refer to index number
newlist[2] = "Modified value"
print (newlist)
#to change range of item values, define new list with new values and refer to range
#of item values ywe want to insert
newlist[0:3] = ["Porche", "Mini", "banana"]	#if we insert more items than replaces, will be inserted
print (newlist)	#if more items, list length will move accordingly

print ()
newlist.insert(2, "other fruit")	#insert() method adds new without replacing
print (newlist)
#add new items to the end of list, we use append() method
newlist.append("End of list item")
print (newlist)
#to append elements from another list to current one, use extend() method
newlist.extend(thislist)	#elements from thislist will be added to end of newlist
print (newlist)
#the extend() can add any iterable object like tuples, sets, dictionaries
thistuple = ("kiwi", "mango")
newlist.extend(thistuple)
print (newlist)

print ()

#we use remove() method to remove specified item
newlist.remove("banana")
print (newlist)
#the pop() method removes the specified index
newlist.pop(0)
print (newlist)
#the del() method also removes specified index
del newlist[1]
print (newlist)
del thislist	#del() can also delete the list completely
#the clear() method empties the list but it remains with no content
newlist1 = ["NEW", "LIST", "TO", "CLEAR"]
print (newlist1)
newlist1.clear()
print (newlist1)	#it still remains without any content

print ()

#we can loop through list items by using for loop
newlist2 = ["NEW", "LIST", "TO", "LOOP", "THROUGH"]
print (newlist2)
for x in newlist2:
	print (x)

print ()

#we can also loop through list items by referring to their index numbers
#this case we use range() and len() functions to create a suitable iterable
for i in range(len(newlist2)):	#the iterable is [0, 1, 2, 3, 4]
	print (newlist2[i])

print ()

#we can also loop list by using a while loop
#we need to determine lenght len() of list, start at 0 and loop list by referring their indexes
i = 0
while i < len(newlist2):
	print (newlist2)
	i = i + 1 	#to increas index by 1 after each interaction. Same as i+=1

#List Comprehension offers shortest syntax for looping through lists
newlist3 = ["ANOTHER", "LIST", "TO", "LOOP"]
[print (x) for x in newlist3]

print ()

""">>List Comprehension offers a shorter syntax when we want to create a new list
based on the values of an existing one:
Example: based on a list of fruits we want a new list containing only the fruits
with the letter "a" in the name

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
mynewlist = []

for x in fruits:		#without List Comprehension we must write for statement
	if "a" in x:		#with a conditional test inside
		mynewlist.append(x)

print (mynewlist)
#with List Comprehension we can do that in one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
mynewlist = [x for x in fruits if "a" in x]

print (mynewlist)

print ()

"""
Syntax>> mynewlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

Condition>> It is ike a filter that only accepts the items that valuate to <True>
	example: Only accept items that are not "apple":
			mynewlist = [x for x in fruits if x != "apple"]
this returns True for all elements other than "apple", making the 
new list contain all fruits except "apple". Condition is optional, can be omitted

Iterable>> It can be any iterable object, like a list, tuple, set
	we can use the range() function to create an iterable:
		newlist = [x for x in range(10)]

Expression>> The expression is the current item in the iteration, but it is 
also the outcome, which you can manipulate before it ends up like a list 
item in the new list

"""
cyber = list(("malware", "ransomware", "trojan", "rootkit"))
print (cyber)
mynewlist1 = [x for x in cyber if x != "malware"]
print (mynewlist1)
#mynewlist1 = [x for x in range(2)]
#print (mynewlist1)
mynewlist1 = [x.upper() for x in cyber]	#Set the values in list to upper case
print (mynewlist1)						#We can set the outcome to whatever
mynewlist1 = ["Hello" for x in cyber]	#Set all values in the new list to 'hello'
print (mynewlist1)
"""
The expression can also contain conditions, not like a filter, but as a way 
to manipulate the outcome:
"""
mynewlist1 = [x if x != "malware" else "phishing" for x in cyber]
print (mynewlist1)	#Return the item if is not malware, if it is malware return phishing
					#if we write malwar, then return original value (malware)

"""
List objects have a sort() method that will sort the list alphanumerically, 
ascending, by default:

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()	#sorts list alphabetically
print (fruits)

numbers = [22, 444, 567, 21, 99, 78]
numbers.sort()
print (numbers)

#To sort descending, use the keyword argument reverse = True:
numbers.sort(reverse = True)
print (numbers)
"""
We can customize our own function by using the keyword argument key = function
The function will return a number that will be used to sort the list (the lowest number first):
"""
def myfunc(n):
	return abs(n - 500)
numbers.sort(key = myfunc)
print (numbers)		#Sort the list based on how close the number is to 500

print ()

"""
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters 
being sorted before lower case letters:
Luckily we can use built-in functions as key functions when sorting a list.
So if we want a case-insensitive sort function, use str.lower as a key function:
"""
cars = ["mini", "audi", "ferrari", "Toyota", "zeta"]
cars.sort()
print (cars) 

cars.sort(key = str.lower)
print (cars)

print ()

"""
What if we want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
"""
cars.reverse()
print (cars)

print ()

"""
We cannot copy a list simply by typing list2 = list1, because: list2 will only 
be a reference to list1, and changes made in list1 will automatically also be 
made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
"""
list1 = ["Carla", "Iaroslava", "Raquel", "Sara"]
list2 = ["Maria", "Sofia"]
list2 = list1.copy()
print (list2)
#Another way to make a copy is to use the built-in method list().
list2 = list(list1)
print (list2)

print ()

"""
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
"""
list3 = list1 + list2
print (list3)
"""
Another way to join two lists are by appending all the items from list2 
into list1, one by one:
"""
for x in list2:
	list1.append(x)
print (list1)
"""
Or we can use the extend() method, which purpose is to add elements 
from one list to another list:
"""
list1.extend(list2)	#Use the extend() method to add list2 at the end of list1:
print (list1)
"""
>>List Methods
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy() 		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list
"""




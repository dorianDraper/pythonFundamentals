#Python ARRAYS
"""
Python does not have built-in support for Arrays, but Python Lists can be used instead.
Heres we use LISTS as ARRAYS, however, to work with arrays in Python wey will have 
to import a library, like the NumPy library.
Arrays are used to store multiple values in one single variable
"""
cars = ["Mini", "Jeep", "Honda"]
print (cars)

"""
An array is a special variable, which can hold more than one value at a time.
If we have a list of items (a list of car names), storing the cars in single variables could look like this:
car1 = "Mini"
car2 = "Jeep"
car3 = "Honda"

However, what if we want to loop through the cars and find a specific one? And what if
we had not 3 cars, but 300? The solution is an array!
An array can hold many values under a single name, and we can access the values by referring to an index number.
"""
#ACCESS elements of an array by referring to the index number
x = cars[1]		#access item 1
print (x)

cars[2] = "Toyota"
print (cars)
print (len(cars))
print (type(cars))

#LOOP array elements by using for in loop

for y in cars:
	print (y)

#ADD elements by using append() method 

cars.append("Renault")
print (cars)

#REMOVE elements by using pop() or remove() methods

cars.pop(1)		#deletes second element
print (cars)

cars.remove("Mini")
print (cars)

"""
>>Array Methods
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
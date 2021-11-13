"""
Python For Loops

A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works 
more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
Example: Print each fruit in a fruit list:
"""
fruits = ["banana", "apple", "orange"]
for x in fruits:	
	print (x)	#The for loop does not require an indexing variable to set beforehand.

"""
Looping Through a String

Even strings are iterable objects, they contain a sequence of characters:
Example: Loop through the letters in the word "banana":
"""
mystr = "Banana"
for x in mystr:
	print (x)
#also can be for x in "Banana": print (x)

"""
The break Statement

With the break statement we can stop the loop before it has looped through all the items:
Example: Exit the loop when x is "Stan":
"""
southPark = ["Cartman", "Kyle", "Kenny", "Stan"]
for x in southPark:
	print (x)		#print comes before the break, this way we display "Kenny" included, see below the difference
	if x == "Kenny":
		break 

print()

for x in southPark:
	if x == "Kyle":	#by doing this, we print only "Cartman"
		break	#Exit the loop when x is "Kyle", but this time the break comes before the print:
	print (x)	

print()

"""
The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:
Example: Do not print Kenny:
"""

for x in southPark:
	if x == "Kenny":
		continue
	print (x)

print()

"""
The range() Function

To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
Example: Using the range() function:
"""
for x in range(6):	#note the range(6) is not the values of 0 to 6, but the values 0 to 5
	print (x)

print()

"""
The range() function defaults to 0 as a starting value, however it is possible 
to specify the starting value by adding a parameter: range(2, 6), which means 
values from 2 to 6 (but not including 6):
Example: Using the start parameter:
"""
for x in range(2, 6):
	print (x)

print()

"""
The range() function defaults to increment the sequence by 1, however it is possible 
to specify the increment value by adding a third parameter: range(2, 30,3)
Example: Increment the sequence with 3 (default is 1):
"""
for x in range(2, 30, 3):
	print (x)

print()

"""
Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
Example: Print all numbers from 0 to 5, and print a message when the loop has ended:
"""
for x in range(6):
	print (x)
else:
	print ("End of this loop")

print()

#The else block will NOT be executed if the loop is stopped by a break statement

"""
Nested Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
Example: Print each color for every fruit:
"""
fruits = ["banana", "mango", "apple"]
colors = ["yellow", "orange", "green"]

for x in colors:
	for y in fruits:
		print (x, y)

print()

"""
The pass Statement

for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.
"""
numbers = [1, 2, 3]
for x in numbers:
	pass	






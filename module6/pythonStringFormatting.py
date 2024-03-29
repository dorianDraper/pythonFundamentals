"""
Python String Formatting

To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.
Sometimes there are parts of a text that you do not control, maybe they come 
from a database, or user input?
To control such values, add placeholders (curly brackets {}) in the text, and run 
the values through the format() method:
Example: Add a placeholder where you want to display the price:
"""
price = 49
txt = "The price is {} dollars"
print (txt.format(price))	#string.format(value1, value2...these are required to be formatted)
"""
You can add parameters inside the curly brackets to specify how to convert the value:
Example: Format the price to be displayed as a number with two decimals:
"""
txt = "The price is {:.2f} dollars"
print (txt.format(price))
"""
The Placeholders

The placeholders can be identified using named indexes {price}, numbered indexes {0}, 
or even empty placeholders {}.
Example: Using different placeholder values:
"""
txt1 = "My name is {fname}, I'm {age}".format(fname = "Jorge", age = 34)
#txt2 = "My name is {0}, I'm {1}".format("John, 36")
txt3 = "My name is {}, I'm {}".format("Richard", 35)
print (txt1)
#print (txt2)
print (txt3)
#More formatting types in https://www.w3schools.com/python/ref_string_format.asp
"""
Multiple Values

If you want to use more values, just add more values to the format() method:
print(txt.format(price, itemno, count))
And add more placeholders:
Example
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print (myorder.format(quantity, itemno, price))
"""
Index Numbers

You can use index numbers (a number inside the curly brackets {0}) 
to be sure the values are placed in the correct placeholders:
Example
"""
myorder = "Now I want {0} pieces of the item number {1} for {2:.2f} dollars"
print (myorder.format(quantity, itemno, price))
"""
Also, if you want to refer to the same value more than once, use the index number:
Example
"""
name = "Jorge"
age = 34
txt = "His name is {0}. {0} is {1} years old"
print (txt.format(name, age))
"""
Named Indexes

You can also use named indexes by entering a name inside the curly brackets {carname}, 
but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
Example
"""
mycar = "I have a {carname}, it is a {model}"
print (mycar.format(carname = "Ford", model = "Mustang"))

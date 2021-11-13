# ==Python Numbers
""" 
>int or integer is whole number positive or negative without decimals
of unlimited lenght
>float or floating point number is positive or negative containing one or
more decimals. Also scientific number with "e" indicate power of 10
>complex numbers are written with a "j" as the imaginay part
"""
# type conversion
x = 1
y = 2.8
z = 1j	#we cannot convert complex numbers into another number type

a = float(x) #convert from int to float
b = int(y) #convert from float to int
c = complex(x) #convert from int to complex

print (a)
print (b)
print (c)

# Random numbers
# it is Python built-in module called random() to make random numbers

import random

print (random.randrange(1, 10))

print ()

myRandom = (random.randrange(10, 30))
print (myRandom)

if myRandom <= 20 and myRandom >= 15:
	print ("The generated random number is between 15 and 20")
elif myRandom > 10 and myRandom < 15:
	print ("This random is between 10 and 15")
else:
	print ("The random number is higher than 20")

print ()

#Python Casting
"""
with Casting we specify a type on to a variable; Python uses classes to
define data types; Casting is done using constructor functions:
	>int() - contructs integer from an integer literal, a float literal (
	by rounding down to the previous whole number), or a string literal
	(providing the string represents a whole number)
	>float() - contructs a float number from an integer literal, a float
	literal or a string literal (providing the string represents a float
	or an integer)
	>str() - contructs a string from a wide variety of data types,
	including strings, integer literals and float literals
"""
x = int(1)	# x will be 1
y = int(2.8)	# y will be 2
z = int("3")	# z will be 3

print ()

x = float(1)	# x will be 1.0
y = float(2.8)	# y will be 2.8
z = float("3")	# z will be 3.0
w = float("4.2")	# w will be 4.2

print ()

x = str("s1")	# x will be 's1'
y = str(2)	# y will be '2'
z = str(3.0)	# z will be '3.0'

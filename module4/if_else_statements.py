"""IF...ELSE 
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.
"""
a = 33
b = 200
if b > a:
	print ("b is greater than a")

#Indentation: Python relies on indentation (whitespace at the beginning of a line) to define scope in the code

"""
ELIF
The elif keyword is pythons way of saying "if the previous conditions were not true, 
then try this condition".
"""
c = 100
d = 500
if c > d:
	print ("c is greater than d")
elif c < d:
	print ("c is less than d")

#ELSE
#else keyword catches anything which isn't caught by the preceding conditions:
a = 200
b = 33
if b > a:
	print ("b is greater than a")
elif a == b:
	print ("a and b are equal")
else:
	print ("a is greater than b")

#Short Hand IF: If have only one statement to execute, can put it on the same line as the if statement.
if a > b: print ("a is greater than b")
#Short Hand IF...ELSE only one statement to execute, one for if, and one for else, then same line:
a = 2
b = 330
print ("A") if a > b else print ("B")
#This technique is known as Ternary Operators, or Conditional Expressions.

a = 330
b = 330
print ("A") if a > b else print ("=") if a == b else print ("B")
#can also have multiple else statements on the same line:

print ()

#AND keyword is logical operator used to combine conditional statements
#test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
	print ("Both conditions are True")

#OR keyword used to combine conditional statements
#test if a is greater than b, OR if a is greater than c
if a > b or a > c:
	print ("At least one of the conditions is True")
    	
#NESTED IF
#we can have if statements inside if statements, this is called nested if statements
x = 19

if x > 10:
	print ("Above ten, ")
	if x > 20:
		print ("and also above 20!")
	else:
		print ("but not above 20.")

#PASS statement
"""
if statements cannot be empty, but if you for some reason have an if statement 
with no content, put in the pass statement to avoid getting an error.
"""
a = 33
b = 200

if b > a:
	pass



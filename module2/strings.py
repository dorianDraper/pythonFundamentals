# ==Python Strings
"""
Strings are surrounded either single quotations '' or double ""

"""

# assign String to a Variable
a = "Hellooo"
print (a)

# Multiple Strings
a = """Lorem ipsum dolor sit amet,	
consectetur adipiscing elit
"""
print (a)	# also works with '''

"""
Strings are Arrays of bytes representing unicode characters. Python has no
character type, single character is simply a string with length of 1
square brackets[] can be used to access elements of the string
"""

a = "Python is awesome"
print (a[5])

print ()

# we can loop through characters in a string with for loop
for x in "banana":
	print (x)

print ()

# String Length
a = "let's go"
print (len(a))

print ()

# to check if certain phrase or character is present in string we use
# keyword in
txt = "My day started with the typical c'mon let's get up boy"
print ("started" in txt)
# also in an if statement
if "get" in txt:
	print ("Yes 'get' is present in txt variable")

print ()

# keyword not to check if phrase or character not present in a string
txt1 = "Best things in life are free"
print ("expensive" not in txt1)
if "expensive" not in txt1:
	print ("Yes 'expensive' is not present in txt1")

print ()

# Slicing Strings
#return a range of characters by using slice syntax
b = "Good morning Vietnam"
print (b[2:5])	#first character has index 0, position 2&5 not there
print (b[ :3])	#from start leave start index empty
print (b[2: ])	#to the end leave out end index
print (b[-5:-2])	#negative indexing to start slice from end of str

print ()

"""Modify Strings
by using built-in methods
"""

c = "Hey my good friend"
print (c.upper())	#upper() returs str in upper case
print (c.lower())	#lower() str in lower case

d = "  Wow we have whitespace here!  "
print (d.strip())	#strip() removes whitespace from beginning or end
e = "Orginal string"
print (d.replace("J", "T"))

print ()

f = "Hello, Darkness"
print (f.split(", "))	#split() splits strs into substrings if separator
conc = c + " " + f 		#concatenate strings
print (conc)

print ()

"""age = 36
txtformat = "My text" + age	#this cannot be combined
print (txtformat)
"""
age = 34
txtformat = "I am {}"	#fomat() takes passed args, formats them and places where {}
print (txtformat.format(age))
myname = "Jorge"
livein = "Banyeres"
multiple = "My name is {}, I live in {} and I am {} old"
print (multiple.format(myname, livein, age))	#format() can receive multiple args
multiple1 = "I live in {1}, my name is {0} and I am {2} old"
print (multiple1.format(myname, livein, age))	#using index numbers {0}

print ()

#Escape Characters
#errortxt = "We are "the people" having fun"	#wrong syntax
righttxt = "We are the \"the people\" having fun"	#backslash to escape characters where not allowed
print (righttxt)
"""
Escape Characters
\' Single quote
\\ Backslash
\n New Line
\r Carriage Return
\t Tab
\b Backspace
\f Form Feed
"\"ooo Octal value
"\"xhh Hex value

"""
"""
String Methods => https://mycourses.w3schools.com/courses/146/pages/2-dot-4-6-string-methods?module_item_id=1687

Method					Description
capitalize()	Converts the first character to upper case
casefold()		Converts string into lower case
center()		Returns a centered string
count()			Returns the number of times a specified value occurs in a string
encode()		Returns an encoded version of the string
endswith()		Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()			Searches the string for a specified value and returns the position of where it was foung
format()		Formats specified values in a string
"""

"""
=Python Booleans
Boolean values to need to know if an expression is True of False
We can evaluate any expression in Python and get one of two answers
When we compare two values the expression is evaluated and Python returns boolean answer

"""
print ()

print (10 > 9)
print (10 == 9)
print (10 < 9)
#when we run a condition in an if statement, Python returns True or False
print ()

a = 200
b = 33

if b > a:
	print ("b is greater than a")
else:
	print ("b is not greater than a")

print ()
"""
==Operators
operators are used to perform operations on variables and values
there are: arithmetic, assignment, comparison, logical, identity, membership,
and bitwise operators
see the operator + to add together two values
"""
print (10 + 5)

"""
==Arithmetic Operators: to perform common mathematical operations
+	Addition
-	Substraction
*	Multiplication
/	Division
%	Modulus
**	Exponentation
//	Floor Division

==Assignment Operators: to assign values to variables
=	 x=5 	x=5
+=	 x+=3 	x=x+3
-=	 x-3 	x=x-3
*=	 x*=3 	x=x*3
/=	 x/=3 	x=x/3
%=	 x%=3 	x=x%3
//=	 x//=3 	x=x//3
**=	 x**=3 	x=x**3
&=	 x&=3 	x=x&3
|=	 x|=3 	x=x|3
>>=	 x>>=3 	x=x>>3
<<=	 x<<=3 	x=x<<3

==Comparison Operators: to compare two values
==	Equal	x==y
!=	Not Equal	x!=y
>	Greater than	x>y
<	Less than	x<y
>=	Greater than or equal to 	x>=y
<=	Less than or equal to 	x<=y

==Logical Operators: to combine conditional statements
and 	Returns True if both statements are true	x<5 and x<10
or 		Returns True if one of statements is true	x<5 or x<4
not 	Reverse result and returns False if result true		not(x<5 and x<10)

==Identity Operators: compare objects, not if they are equal bur if they are
actually the same object with same memory localion
is 	Returs True if both variables are the same object 	x is y
is not 	Returns True if both variables are not the same object 	x is not y

==Membership Operators: used to test if a sequence is presented in an object
in 	Returns True if sequence with specified value is present in the object x in y
not in 	Returns True if a sequence with specified value is no present 	x not in y

==Bitwise Operators: to compare (binary) numbers
&	AND 	Sets each bit to 1 if both bits are 1
| 	OR 		Sets each bit to 1 if one of two bits is 1
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let leftmost bits fall off
>> 	Signed right shift 		Shift right by pushing copies of the leftmost bit in from the left 
							and let the rightmost bits fall off

"""

#evaluate values and variables using bool() function which gives T/F in return
print (bool("Hello"))
print (bool(15))

x = "Hello"
y = 15

print (bool(x))
print (bool(y))
"""most values are true if have some sort of content:
any string is true except if empty
any number is true except 0
any list, tuple,set, dict are true except empty ones
also the value non is false

"""
#Functions can return a boolean
def myfunc():
	return True

print (myfunc())
#we can execute code based on the Boolean answer of a function:

print ()

def myfunc1():
	return True

if myfunc1():
	print("YES!")	#print YES! if function returns True, otherwise NO!!
else:
	print("NO!!")

print ()

#the isinstance() function can determine if object is of certain data type and return boolean value
x = 200
print (isinstance(x, int))


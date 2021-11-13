# Unpacking a collection
# collection of values in a list, tupple, values can be extracted into variables
fruits = ["apple", "orange", "cherry"]
x, y, z = fruits
print ("First fruit in list is " + x)
print (y)
print (z)
print (x, y, z)
print ()
variable1 = "Python is "
variable2 = "awesome"
variable3 = variable1 + variable2
print (variable3)
print ()
# Global variables
"""
those created outside of a function
can be used for everyone both inside and outside of functions
"""
globalVariable = "awesome"

def myfunc():
	print ("Python is " + globalVariable)

myfunc()
"""
if we create variable with same value inside a function this will be local
and can only be used inside the function; the global one will remain
as it was, global and original value
"""
print ()
newVariable = "global"

def myfunc1():
	newVariable1 = "local"
	print ("This variable is " + newVariable1 + ", instead")

myfunc1() 

print ("This variable is " + newVariable)

"""
normally variables inside function are local, to create global inside
a function we use <global> keyword
"""
print ()

def myfunc2():
	global thisVariable
	thisVariable = "Fantastic"

myfunc2()

print ("Python is also " + thisVariable)
"""
also use <global> keyword to change the value of global variable inside
a function
"""
print ()

# thisVariable1 = "amazing"

def myfunc3():
	global globalVariable
	globalVariable = "so cool"

myfunc3()

print ("If that was not enough, Python is " + globalVariable)



x = 5
y = "5"
print (x + y)

"""
Python Lambda

A lambda function is a small anonymous function. A lambda function can take any number of arguments, 
but can only have one expression.

lambda arguments : expression
The expression is executed and the result is returned:
"""
x = lambda a : a + 10	#Add 10 to argument a, and return the result:
print (x(5))

x = lambda a, b : a * b 	#Multiply argument a with argument b and return the result:
print (x(5, 6))

x = lambda a, b, c : a + b + c 	#Summarize argument a, b, and c and return the result:
print (x(5, 6, 2))

"""
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied 
with an unknown number:
"""
def myfunc(n):
	return lambda a : a * n 

mydoubler = myfunc(2)

print (mydoubler(4))

#Use that function definition to make a function that always doubles the number you send in, or treble it

#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
	return lambda a : a * n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print (mydoubler(11))
print (mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.
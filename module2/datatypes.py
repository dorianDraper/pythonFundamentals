# Module 2 - Data Types

"""
text type = str
numeric types = int, float, complex
sequence types = list, tupple, range
mapping type = dict
set types = set, frozenset
boolean type = bool
bynary types = bytes, bytearray, memoryview
"""

# getting data type
#x = 5
#print (type(x))

print ()

x = "Hello there" # same x = str("Hello there")
print (x)
print (type(x))

print()

x = 20 # same x = 20
print (x)
print (type(x))

print ()

x = float(20.5) # same x = 20.5
print (x)
print (type(x))

print ()

x = complex(1j) # same x = 1j
print (x)
print (type(x))

print ()

x = list(("apple", "orange", "cherry")) # same x = ["apple", "orange"]
print (x)
print (type(x))

print ()

"""x = tuple(("Mini", "BMW", "Porche")) # same x = ("Mini", "BMW")
print (x)
print (type(x))
"""
print ()

x = range(6) # same x = range(6)
print (x)
print (type(x))

print ()

x = dict(name="John", age=36) # same x = {"name" : "John", "age" : 36}
print (x)
print (type(x))

print ()

x = set(("banana", "mango", "papaya")) # same x = {"banana", "mango"}
print (x)
print (type(x))

print ()

x = frozenset(("fruit", "bread", "meat")) # same x = frozenset ({"fruit"})
print (x)
print (type(x))

print ()

x = bool(5) # same x = True
print (x)
print (type(x))

print ()

x = bytes(5) # same x = b"Hello"
print (x)
print (type(x))

print ()

x = bytearray(5) # same x = bytearray(5)
print (x)
print (type(x))

print ()

x = memoryview(bytes(5)) # same x = memoryview(bytes(5)) 
print (x)
print (type(x))






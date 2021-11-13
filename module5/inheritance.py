"""
Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

>>Parent class is the class being inherited from, also called base class.
>>Child class is the class that inherits from another class, also called derived class.
"""
"""
Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class:
"""
class Person:
	def __init__(self, fname, lname):	#init function is called automatically every time used to create a new object
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

#Use the Person class to create an object and then execute the printname method

x = Person("John", "Doe")
x.printname()

"""
Create a Child Class

To create a class that inherits the functionality from another class, send the parent class 
as a parameter when creating the child class. Student, which will inherit the properties 
and methods from the Person class:

Now the Student class has the same properties and methods as the Person class.
"""

class Student(Person):
	pass	#the pass keyword when you do not want to add any other properties/methods to the class

x = Student("Mike", "Olsen")
x.printname()

"""
Add the __init__() Function

So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
"""
"""class Student(Person):
	def __init__(self, fname, lname):	"""

"""
When we add the init function, the child class will no longer inherit the parent's function
The child's init function overrides the inheritance of the parent's init function
To keep the inheritance of the parent's init function, add a call to the parent's function
"""
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)

"""
Now we have added the init function and kept the inheritance of the parent class and we 
are ready to add functionality in the init function
"""
"""
Use the super() Function

Python also has a super() function that will make the child class inherit all 
the methods and properties from its parent: By using the super() function, you do not have to use 
the name of the parent element, it will automatically inherit the methods and properties from its parent.

Now let's add properties: property graduationyear to Student class
"""
class Student(Person):
	def __init__(self, fname, lname, year):	#add the year parameter and pass the year when create objects
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Jane", "Doe", 2019)
x.welcome()






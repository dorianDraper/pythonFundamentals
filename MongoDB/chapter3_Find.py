"""
MongoDB Find

In MongoDB we use the << find >> and << findOne >> methods to find data in a collection.
Just like the SELECT statement is used to find data in a table in a MySQL database.

Find One

To select data from a collection in MongoDB, we can use the << find_one() >> method.
The find_one() method returns the first occurrence in the selection.
Example: Find the first document in the customers collection:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb1 = myclient["nestleGlobal"]
newcol = mydb1["employees"]

employees1 = [
    {"name": "Jorge", "position": "Risk&Compliance Specialist"},
    {"name": "Carol", "position": "CyberSecurity Awareness"},
    {"name": "Manu", "position": "Team Lead"},
    {"name": "Rafa", "position": "CSOC Lead"},
    {"name": "Oliver", "position": "PM Compliance"},
    {"name": "Marc", "position": "Risk Lead"},
    {"name": "Cecilia", "position": "Risk Specialist"},
    {"name": "keyla", "position": "Compliance Specialist"}
]

x = newcol.insert_many(employees1)

print (x.inserted_ids)
print (mydb1.list_collection_names())

findemployee = newcol.find_one()
print (findemployee)
"""
Find All

To select data from a table in MongoDB, we can also use the find() method.
The find() method returns all occurrences in the selection.
The first parameter of the find() method is a query object.
In this example we use an empty query object, which selects all documents in the collection.
No parameters in the find() method gives you the same result as SELECT * in MySQL.
Example: Return all documents in the "customers" collection, and print each document:
"""
for x in newcol.find():
    print (x)

print()
"""
Return Only Some Fields

The second parameter of the find() method is an object describing which fields to include in the result.
This parameter is optional, and if omitted, all fields will be included in the result.
Example: Return only the names and addresses, not the _ids:
"""
for x in newcol.find({}, {"_id": 0, "name": 1, "position": 1}):
    print (x)
"""
You are not allowed to specify both 0 and 1 values in the same object
(except if one of the fields is the _id field).
If you specify a field with the value 0, all other fields get the value 1, and vice versa:
Example: This example will exclude "id" and "name" from the result:
"""
for x in newcol.find({}, {"_id": 0, "name": 1, "position": 1}):
    print (x)
#for x in newcol.find({}, {"_id": 0, "name": 0}): #print only position
    #print (x)

print()
"""
MongoDB Query
Filter the Result

When finding documents in a collection, you can filter the result by using a query object.
The first argument of the find() method is a query object, and is used to limit the search.
Example: Find document(s) with the position "Compliance Specialist":
"""
myquery = {"name": "Oliver"}
mydoc = newcol.find(myquery)
for x in mydoc:
    print (x)

newcol.drop()

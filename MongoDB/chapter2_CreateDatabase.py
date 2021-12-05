"""
MongoDB Create Database

To create a database in MongoDB, start by creating a MongoClient object, then specify
a connection URL with the correct ip address and the name of the database you want to create.

MongoDB will create the database if it does not exist, and make a connection to it.
Example: Create a database called "mydatabase":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/") #MongoClient object

mydb = myclient["mydatabase"]   #Create a database called "mydatabase"
"""
Important: In MongoDB, a database is not created until it gets content!

MongoDB waits until you have created a collection (table), with at least
one document (record) before it actually creates the database (and collection).

Check if Database Exists

Remember: In MongoDB, a database is not created until it gets content, so if
this is your first time creating a database, you should complete the next two chapters
(create collection and create document) before you check if the database exists!

You can check if a database exist by listing all databases in you system:
Example: Return a list of your system's databases:
"""
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print ("The db exists")
else:
    print ("The db does not exist")
"""
Or you can check a specific database by name:
Example: Check if "mydatabase" exists:
"""
"""
================================================================================
"""
"""
MongoDB Create Collection

A collection in MongoDB is the same as a table in SQL databases.

Creating a Collection

To create a collection in MongoDB, use database object and specify the name of
the collection you want to create. MongoDB will create the collection if it does not exist.
Example: Create a collection called "customers":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["customers"]
"""
Important: In MongoDB, a collection is not created until it gets content!

MongoDB waits until you have inserted a document before it actually creates the collection.

Check if Collection Exists

Remember: In MongoDB, a collection is not created until it gets content,
so if this is your first time creating a collection, you should complete the
next chapter (create document) before you check if the collection exists!
You can check if a collection exist in a database by listing all collections:
Example: Return a list of all collections in your database:
"""
print(mydb.list_collection_names())
"""
Or you can check a specific collection by name:
Example: Check if the "customers" collection exists:
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
"""
collist = mydb.list_collection_names()
if "customers" in collist:
    print ("The collection exists")
else:
    print ("The collection does not exist")

print()
"""
MongoDB Insert

A document in MongoDB is the same as a record in SQL databases.

Insert Into Collection

To insert a record, or document as it is called in MongoDB,
into a collection, we use the << insert_one() >> method.

The first parameter of the insert_one() method is a dictionary containing
the name(s) and value(s) of each field in the document you want to insert.
Example: Insert a record in the "customers" collection:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name": "Jorge", "position": "Risk&Compliance Specialist"}

x = mycol.insert_one(mydict)
"""
Return the _id Field

The << insert_one() >> method returns a InsertOneResult object,
which has a property, inserted_id, that holds the id of the inserted document.
Example: Insert another record in the "customers" collection, and return the value of the _id field:
"""
mydict2 = {"name": "Carol", "position": "CyberSecurity Awareness"}
x1 = mycol.insert_one(mydict2)
print (x.inserted_id)
print (x1.inserted_id)
"""
If you do not specify an _id field, then MongoDB will add one
for you and assign a unique id for each document.
In the example above no _id field was specified, so MongoDB assigned a unique _id
for the record (document).

Insert Multiple Documents

To insert multiple documents into a collection in MongoDB, we use the << insert_many() >> method.

The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:
Example
"""
mydict3 = [
    {"name": "Manu", "position": "Team Lead"},
    {"name": "Rafa", "position": "CSOC Lead"},
    {"name": "Oliver", "position": "PM Compliance"},
    {"name": "Marc", "position": "Risk Lead"},
    {"name": "Cecilia", "position": "Risk Specialist"},
    {"name": "keyla", "position": "Compliance Specialist"}
]

x = mycol.insert_many(mydict3) #returns a InsertManyResult object, which has a property, inserted_ids
print (x.inserted_ids) ##print list of the _id values of the inserted documents:

print()
"""
The << insert_many() >> method returns a InsertManyResult object,
which has a property, inserted_ids, that holds the ids of the inserted documents.
Insert Multiple Documents, with Specified IDs
If you do not want MongoDB to assign unique ids for you document,
you can specify the _id field when you insert the document(s).
Remember that the values has to be unique. Two documents cannot have the same _id.
Example
"""
mydict4 = [
    {"_id": 1, "name": "Jorge", "position": "Risk&Compliance Specialist"},
    {"_id": 2, "name": "Carol", "position": "CyberSecurity Awareness"},
    {"_id": 3, "name": "Manu", "position": "Team Lead"},
    {"_id": 4, "name": "Rafa", "position": "CSOC Lead"},
    {"_id": 5, "name": "Oliver", "position": "PM Compliance"},
    {"_id": 6, "name": "Marc", "position": "Risk Lead"},
    {"_id": 7, "name": "Cecilia", "position": "Risk Specialist"},
    {"_id": 8, "name": "keyla", "position": "Compliance Specialist"}
]

x = mycol.insert_many(mydict4)
print (x.inserted_ids)

print()
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
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict4 = [
    {"_id": 1, "name": "Jorge", "position": "Risk&Compliance Specialist"},
    {"_id": 2, "name": "Carol", "position": "CyberSecurity Awareness"},
    {"_id": 3, "name": "Manu", "position": "Team Lead"},
    {"_id": 4, "name": "Rafa", "position": "CSOC Lead"},
    {"_id": 5, "name": "Oliver", "position": "PM Compliance"},
    {"_id": 6, "name": "Marc", "position": "Risk Lead"},
    {"_id": 7, "name": "Cecilia", "position": "Risk Specialist"},
    {"_id": 8, "name": "keyla", "position": "Compliance Specialist"}
]

x = mycol.insert_many(mydict4)
colres = mycol.find_one()
print (colres)

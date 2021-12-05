import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["building2"]
thiscol = mydatabase["employees"]

employeesList = [
    {"name": "Jorge", "position": "Risk&Compliance Specialist"},
    {"name": "Carol", "position": "CyberSecurity Awareness"},
    {"name": "Manu", "position": "Team Lead"},
    {"name": "Rafa", "position": "CSOC Lead"},
    {"name": "Oliver", "position": "PM Compliance"},
    {"name": "Marc", "position": "Risk Lead"},
    {"name": "Cecilia", "position": "Risk Specialist"},
    {"name": "keyla", "position": "Compliance Specialist"}
]

x = thiscol.insert_many(employeesList)

print (mydatabase.list_collection_names())
print (x.inserted_ids)
x = thiscol.find_one()
print (x)
for x in thiscol.find():
    print (x)

print()
"""
MongoDB Query
Filter the Result

When finding documents in a collection, you can filter the result by using a query object.
The first argument of the find() method is a query object, and is used to limit the search.
Example: Find document(s) with the position "Compliance Specialist":
"""
addnew = {"name": "Christian", "position": "Compliance Specialist"}
#x = thiscol.insert_one(addnew)

myquery = {"position": "Compliance Specialist"}
mydoc = thiscol.find(myquery)

for x in mydoc:
    print (x)

print()
"""
Advanced Query

To make advanced queries you can use modifiers as values in the query object.
E.g. to find the documents where the "address" field starts with the letter "S"
or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
Example: Find documents where the position starts with the letter "R" or higher:
"""
myquery1 = { "position" : { "$gt" : "R" } }
mydoc1 = thiscol.find(myquery1)

for x in mydoc1:
    print (x)

print()
"""
Filter With Regular Expressions

You can also use regular expressions as a modifier.
Regular expressions can only be used to query strings.
To find only the documents where the "position" field starts with the letter "P",
use the regular expression {"$regex": "^P"}:
Example: Find documents where the address starts with the letter "P":
"""
myquery2 = { "position" : { "$regex" : "^P" } }
mydoc2 = thiscol.find(myquery2)

for x in mydoc2:
    print (x)

print()
"""
MongoDB Sort

Use the << sort() >> method to sort the result in ascending or descending order.
The sort() method takes one parameter for "fieldname" and one parameter for "direction"
(ascending is the default direction).
Example: Sort the result alphabetically by name:
"""
addnews = [
    {"name": "Aleyda", "position": "CSOC"},
    {"name": "Bibian", "position": "DataAnalyst"},
    {"name": "Carlos", "position": "CSOC"},
    {"name": "David", "position": "DPO"}
]

#x = thiscol.insert_many(addnews)  we add some names starting from "A" to sort

"""for y in thiscol.find(): #print the new names added to be sorted
    print (y)
    mysort = thiscol.find().sort("name") #result in ascending order
    for x in mysort:
        print(x)

    print()"""
"""
Sort Descending

Use the value -1 as the second parameter to sort descending.
sort("name", 1) #ascending
sort("name", -1) #descending
Example: Sort the result reverse alphabetically by name:
"""
    #mysort1 = thiscol.find().sort("name", -1)
    #for x in mysort1:
    #    print(x)

print()
"""
MongoDB Delete

To delete one document, we use the << delete_one() >> method.
The first parameter of the delete_one() method is a query object defining which document to delete.
Note: If the query finds more than one document, only the first occurrence is deleted.
Example: Delete the document with the address "Mountain 21":
"""
    #myquery = { "name": "Aleyda" }
    #thiscol.delete_one(myquery)
"""
Delete Many Documents

To delete more than one document, use the << delete_many() >> method.
The first parameter of the delete_many() method is a query object defining which documents to delete.
Example: Delete all documents were the position starts with the letter C:
"""
    #myquery = { "position" : { "$regex" : "^C" } }
    #x = thiscol.delete_many(myquery)
    #print (x)
    #print (x.deleted_count, "documents deleted.")
"""
Delete All Documents in a Collection

To delete all documents in a collection, pass an empty query object to the << delete_many() >> method:
Example: Delete all documents in the "customers" collection:
"""
    #x = thiscol.delete_many({})
    #print (x.deleted_count, "documents deleted.")
"""
MongoDB Drop Collection

You can delete a table, or collection as it is called in MongoDB, by using the << drop() >> method.
Example: Delete the "customers" collection:
"""
    #thiscol.drop()
"""
The drop() method returns true if the collection was dropped successfully,
and false if the collection does not exist.
"""
"""
MongoDB Update

You can update a record, or document as it is called in MongoDB, by using the << update_one() >> method.
The first parameter of the update_one() method is a query object defining which document to update.
Note: If the query finds more than one record, only the first occurrence is updated.
The second parameter is an object defining the new values of the document.
Example: Change the position from "Valley 345" to "Canyon 123":
"""
myquery = { "position" : "Risk&Compliance Specialist" }
newvalues = { "$set": { "position": "CSOC Analyst" } }

thiscol.update_one(myquery, newvalues)

for x in thiscol.find():
    print (x)
"""
Update Many

To update all documents that meets the criteria of the query, use the << update_many() >> method.
Example: Update all documents where the position starts with the letter "C":
"""
myquery = { "position": { "$regex": "^C" } }
newvalues = { "$set": { "position": "CyberSecurity Specialist"}}

thiscol.update_many(myquery, newvalues)

for x in thiscol.find():
    print (x)
x = thiscol.update_many(myquery, newvalues)
print (x.modified_count, "documents updated.")

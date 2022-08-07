import pymongo

client = pymongo.MongoClient("mongodb+srv://Shivprasad:Shivpi99@shivprasad.bkgom.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d ={
    "name" : "shiv",
    "email" : "shiv@gmail.com",
    "surname":"hiremath"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
import pymongo

client = pymongo.MongoClient("mongodb+srv://Aswini:Aditya0509@cluster0.z0n3j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "Name":"Aswini",
    "emailid" : "aswini0509@gmail.com",
    "surname" : "kumar"
}

db1 = client['mongodb']
coll = db1["test"]
coll.insert_one(d)
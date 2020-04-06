from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

# db.people.update_many(찾을조건,{'$set':어떻게바꿀지})

db.users.update_one({'name':'hobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'hobby'})
print(user)
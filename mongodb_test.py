import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient["run"]
collection = dblist['my_collection']
dic = {'name':'serena',"id":1532}
collection.insert_one(dic)
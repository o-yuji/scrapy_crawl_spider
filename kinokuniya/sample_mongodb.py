import pymongo

client = pymongo.MongoClient('mongodb+srv://yuji:Mii103210@cluster0.qekaxt1.mongodb.net/?retryWrites=true&w=majority')
db = client['BOOKDB']
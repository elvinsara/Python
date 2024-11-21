from pymongo import MongoClient

uri = r"mongodb+srv://elvinsaraeldho:CkWZ0WHHf1HlsEQ7@cluster0.udhei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client= MongoClient(uri)
    print("connected to mongo")
    db = client['sample_mflix']
    collection = db['movies']
    results = collection.find()
    for doc in results:
        print(doc)
        break
except Exception as e:
    print(e)
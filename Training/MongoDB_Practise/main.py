# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# print(1)
# client = MongoClient(uri,server_api=ServerApi('1'),tlsAllowInvalidCertificates=True)
# print(2)
# try:
#     client.admin.command('ping')
#     print(3)
#     print("connection successful")
# except Exception as e:
#     print(e)
# 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://elvinsaraeldho:CkWZ0WHHf1HlsEQ7@cluster0.udhei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
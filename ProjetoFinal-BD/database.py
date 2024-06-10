import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://franciscogsilverio:zLus3awo5KLxsUgF@cluster0.g96z7on.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            # self.db.drop_collection(self.collection)
            # self.collection.insert_many(dataset)
            print("Banco de dados resetado")
        except Exception as e:
            print(e)

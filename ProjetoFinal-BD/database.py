import pymongo


class Database:
    def __init__(self, database, collection, name):
        self.name = name
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
            print(f"Conectado à coleçao, {self.name}")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print(f"Coleção {self.name} resetada com sucesso!")
        except Exception as e:
            print(e)

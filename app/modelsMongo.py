from pymongo import MongoClient

mongoConnection = {
    'server': 'ace-dbserver',
    'port': 27017,
    'username': 'root',
    'password': 'root'
}

class Schema:
    def __init__(self):
        self.client = MongoClient(
            mongoConnection['server'],
            mongoConnection['port'],
            username=mongoConnection['username'],
            password=mongoConnection['password']
        )
        self.db = self.client['ace_todo_db']
        self.create_to_do_collection()


    def create_to_do_collection(self):
        try:
            colla = {'locale': 'en_US', 'strength': 2, 'numericOrdering': True, 'backwards': False}
            collection_name = 'ace_todo_collection'

            col = self.db.create_collection(
                name=collection_name,
                codec_options=None,
                read_preference=None,
                write_concern=None,
                read_concern=None,
                session=None,
                collation=colla
            )
        except Exception as err:
            if "already exists" in err._message:
                col = self.db[collection_name]
            else:
                print ("create_collection() ERROR:", err)
                col = None

        print ("Collection name:", col.name)


class ToDoModel:

    def __init__(self):
        self.client = MongoClient(
             mongoConnection['server'],
             mongoConnection['port'],
             username=mongoConnection['username'],
             password=mongoConnection['password']
         )
        self.db = self.client['ace_todo_db']
        self.collection = self.db['ace_todo_collection']


    def create(self, params):
        doc1 = {'title': params['title']}
        self.collection.insert_one(doc1)
        return 'ok'


    def list_items(self, where_clause=""):
        resut = []

        for doc in self.collection.find():
            resut.append(doc["title"])

        return resut

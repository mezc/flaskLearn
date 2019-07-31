import pymongo

MONGO_URL = '127.0.0.1'
MONGO_DB = "jikexueyuan" #数据库名称
MONGO_TABLE = "user_collection" #表单名称

def get_collection():
  client = pymongo.MongoClient(MONGO_URL)
  db = client[MONGO_DB]
  user_collection = db[MONGO_TABLE]
  return user_collection

class User():
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def save(self):
    user_info = {
      "name": self.name,
      "email": self.email
    }

    collection = get_collection()
    id  = collection.insert(user_info)
    print(id)
    
  @staticmethod
  def query_users():
    users = get_collection().find()
    return users



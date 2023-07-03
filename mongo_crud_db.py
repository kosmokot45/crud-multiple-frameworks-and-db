################## EXAMPLES

####### Create

# new_show = {
#     "name": "Vladimir",
#     "age": 29
# }
# print(create_data(series_collection, new_show))

####### Read

# result = read_data(series_collection, {'age': 25}, multiple=True)
# print(result)

####### Update

# id = preparing_id(series_collection, {'name': 'Vasiliy'})
# update_data(series_collection, {'_id':id}, {'name':'Narek'})

####### Delete

# id = preparing_id(series_collection, {'name': 'Narek'})
# delete_data(series_collection, {'_id': id})


from pymongo import MongoClient
import settings

host = settings.mongodb_host
port = int(settings.mongodb_port)
client = MongoClient(host, port)

db = client['seriesdb']
series_collection = db['users']

def preparing_id(collection, data):
    data_info = read_data(collection, data)
    id_ = data_info['_id']
    return id_

def create_data(collection, data):
    return collection.insert_one(data).inserted_id

def read_data(collection, data, multiple=False):
    if multiple:
        results = collection.find(data)
        return [r for r in results]
    else:
        return collection.find_one(data)

def update_data(collection, query_data, updated_values):
    collection.update_one(query_data, {'$set': updated_values})

def delete_data(collection, data):
    collection.delete_one(data)

# import pymongo
# import json
# import os
# from pymongo import MongoClient, InsertOne


# # Connection to the MongoDB
# MONGODB_URI = os.getenv('MONGODB_URI')
# DB_NAME = os.getenv('DB_NAME')
# DB_COLLECTION = os.getenv('DB_COLLECTION')
# EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL') or 'keepitreal/vietnamese-sbert'

# client = pymongo.MongoClient(MONGODB_URI)
# db = client[DB_NAME]
# collection = db[DB_COLLECTION]
# requesting = []

# # embed the data to key embeding
# from sentence_transformers import SentenceTransformer
# embedding_model = SentenceTransformer(EMBEDDING_MODEL)

# #load data from mongodb
# cursor = collection.find({})
# for item in cursor:
#     # Generate the embedding for the product properties
#     item['embedding'] = embedding_model.encode(, convert_to_tensor=True).tolist()
#     requesting.append(InsertOne(item))

# # Update the collection with the new embeddings
# result = collection.bulk_write(requesting)

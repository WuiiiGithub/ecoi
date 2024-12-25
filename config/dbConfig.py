from pymongo import MongoClient
from config import DATABASE

def getDB():
    return MongoClient(DATABASE['connectionString'])[DATABASE['dbName']]

def getCollection(name: str):
    return getDB()[name]
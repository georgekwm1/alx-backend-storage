#!/usr/bin/env python3

""" A Python function that lists all documents in a collection"""
from pymongo import MongoClient
import pprint


def list_all(mongo_collection):
    """Returns a list of  all documents"""
    # client = MongoClient()
    # db = client.my_db
    new_list = []
    # mongo_collection = db.mongo_collection
    if mongo_collection == None:
        return []
    else:
        for item in mongo_collection.find():
            new_list.append(item)
        return new_list

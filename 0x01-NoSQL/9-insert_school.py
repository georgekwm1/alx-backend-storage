#!/usr/bin/env python3

""" A Python function that inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient
import pprint


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

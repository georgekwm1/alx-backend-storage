#!/usr/bin/env python3

""" A Python function that  changes all topics of a school document based on the name"""
from pymongo import MongoClient
import pprint


def update_topics(mongo_collection, name, topics):
    '''update topics of a school document based on the nam.
    '''
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})

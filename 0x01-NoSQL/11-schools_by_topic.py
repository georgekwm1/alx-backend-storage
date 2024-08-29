#!/usr/bin/env python3
""" A Python function that  returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    '''update topics of a school document based on the nam.
    '''
    result = mongo_collection.find({"topics": topic})
    return [output for output in result]

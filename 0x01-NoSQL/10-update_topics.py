#!/usr/bin/env python3
""" a module that changes all topics of a school"""


def update_topics(mongo_collection, name, topics):
    """
    A function that changes all topics of a school document
    Args:
        mongo_collection: pymongo collection object
        name: (string) will be the school name to update
        topics: (list of str) will be the list of topics approached
    Returns:
    """
    filter_criteria = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    result = mongo_collection.update_one(filter_criteria, update_operation)
    return result

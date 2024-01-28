#!/usr/bin/env python3
"""a module that returns the list of school"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that return list of school having a specific topics
    Args:
        mongo_collection: pymongo collection object
        topic: (string) will be topic searched
    """
    filter_criteria = {"topics": {"$eq": [topic]}}
    result = mongo_collection.find(filter_criteria)
    return list(result)

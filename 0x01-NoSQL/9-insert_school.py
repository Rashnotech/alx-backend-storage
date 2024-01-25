#!/usr/bin/env python3
""" a module that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that inserts a new document in a collection based
    Args:
        mongo_collection: collection document
        kwargs: key word argument i.e dict
    Returns:
        a new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

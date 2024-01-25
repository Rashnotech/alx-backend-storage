#!/usr/bin/env python3
""" a module that lists all documents in a collection """


def list_all(mongo_collection):
    """
    A function that lists all documents in a collection
    Args:
        mongo_collection: a list
    Return:
        an empty list if no document in the collection otherwise list
    """
    return mongo_collection.find()

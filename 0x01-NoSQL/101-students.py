#!/usr/bin/env python3
"""a module that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    A function that returns all students sorted by average score
    Args:
        mongo_collection: a list of all students
    Return:
        an average score
    """
    return mongo_collection.aggregate([{'$project': {
        'name': 1,
        'topics': 1,
        'averageScore': {'$avg': '$topics.score'}
        }},
        {'$sort': {'averageScore': -1}}])

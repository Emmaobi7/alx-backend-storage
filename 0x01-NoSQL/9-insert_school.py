#!/usr/bin/env python3
"""
insert a document
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school: inserts a new doc in a collection
    Args:
       mongo_collection: pymong collection
       kwargs: keys and values
    return: _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id

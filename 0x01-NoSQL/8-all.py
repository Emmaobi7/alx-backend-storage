#!/usr/bin/env python3
"""
list all documents
"""


def list_all(mongo_collection):
    """
    list_all: lists all db collectiions
    args:
        mongo_collection: pymongo collection object
    return: list
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())

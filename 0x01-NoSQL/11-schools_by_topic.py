#!/usr/bin/env python3
"""
where can i learn python
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic: list of scools with topic
    Args:
        mongo_collection: pymongo collection
        topic: will be topic searched
    return: list
    """

    return mongo_collection.find({"topics": topic})

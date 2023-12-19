#!/usr/bin/env python3
"""
upate school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics: update school topics in db
    Args:
        mongo_collecti: pymongo collection
        name: string
        topis: list of string
    """

    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})

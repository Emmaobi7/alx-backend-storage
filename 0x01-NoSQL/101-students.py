#!/usr/bin/env python3
"""
top students
"""


def top_students(mongo_collection):
    """
    top_students: sorted by average score
    return: all students
    """
    return mongo_collection.aggregate([{"$project":
                                      {"name": "$name", "averageScore":
                                       {"$avg": "$topics.score"}}},
                                       {"$sort": {"averageScore": -1}}])

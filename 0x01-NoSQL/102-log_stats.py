#!/usr/bin/env python3
"""
log stats
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(f"{logs.count_documents({})} logs")
    print('Methods:')
    print(f"\tmethod GET: {logs.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {logs.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {logs.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {logs.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {logs.count_documents({'method': 'DELETE'})}")
    count = logs.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{count} status check")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}}
    ]
    top = logs.aggregate(pipeline)
    print("IPs:")
    for top_ip in top:
        ip, count = top_ip.get('ip'), top_ip.get('count')
        print(f"\t{ip}: {count}")

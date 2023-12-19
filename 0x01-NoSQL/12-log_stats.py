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

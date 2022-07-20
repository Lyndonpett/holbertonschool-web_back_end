#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def loggedStats():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs

    nginxLogs = db.nginx

    print(f"{nginxLogs.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"\tmethod {method}: " +
              f"{nginxLogs.count_documents({'method': method})}")

    print(f"{nginxLogs.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    loggedStats()

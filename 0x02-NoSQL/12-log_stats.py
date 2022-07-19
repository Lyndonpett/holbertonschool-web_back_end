#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def loggedStats():
    """provides some stats about Nginx logs stored in MongoDB"""
    # connect to MongoDB and get logs
    client = MongoClient()
    db = client.logs

    # get nginx logs
    nginxLogs = db.nginx

    # print number of docs in the collection
    print(f"{nginxLogs.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # loop each method and print docs with that method
    for method in methods:
        print(f"\tmethod {method}: " +
              f"{nginxLogs.count_documents({'method': method})}")

    # print the number of documents with method=GET and path=/status
    print(f"{nginxLogs.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    loggedStats()

#!/usr/bin/env python3
"""a module that provides some stats about Nginx log"""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    lognx = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('{} logs'.format(lognx.count_documents({})))
    print('Methods:')

    for method in methods:
        count = lognx.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))
    print('{} status check'.format(
                        lognx.count_documents({'method': 'GET',
                                              'path': '/status'})))

#!/usr/bin/env python3
"""a module that provides some stats about Nginx log"""


if __name__ == '__main__':
    from pymongo import MongoClient

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
    print("IPs:")
    ips = lognx.aggregate([{
        '$group': {
            '_id': '$ip',
            'count': {'$sum': 1}
            }
        }, {'$sort': {'count': -1}}, {'$limit': 10}])

    for ip in ips:
        print('\t {}: {}'.format(ip['_id'], ip['count']))

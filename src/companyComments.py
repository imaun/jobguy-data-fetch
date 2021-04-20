import json

class Company(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

companies = []

with open('companies.json') as jsonFile:
    data = json.load(jsonFile)
    for record in data.values():
        companies.append(Company(record))



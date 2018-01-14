import json

with open('C:\\classes.json') as data_file:
    data = json.load(data_file)
    for p in data["class"]:
        print('Name: ' + p['name'])

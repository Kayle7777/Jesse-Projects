#!/bin/python3

import json
import codecs

# Returns all entities in a subset section of a json file. For example, every branch on the tree, but no sub branches on the ones returned
# Example Windows usage: print(jsonwriter('C:\\classes.json','class','name'))
# Example Mac usage: print(jw.jw('/Users/jessew/Downloads/TheGiddyLimit.github.io-master/data/classes.json','class','name'))
def jw(file, d, subd):
    list = []
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        for x in data[d]:
            list.append(x[subd])
    return list

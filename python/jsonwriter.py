#!/bin/python3

import json
import codecs

def jsonopener(file, d, subd):
    list = []
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        for x in data[d]:
            list.append(x[subd])
    return list

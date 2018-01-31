import random, json, codecs
from collections import defaultdict
from itertools import chain

file = "data/backgrounds.json"
def rolljson(t):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        bglist = [list(data[t][l]["name"])]
        return bglist

print(rolljson("background"))

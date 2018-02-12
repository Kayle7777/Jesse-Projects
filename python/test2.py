import random, json, codecs
from collections import defaultdict
from itertools import chain
from pprint import *
import objectpath

"""file = "data/background.json"
with codecs.open(file, "r", "utf-8-sig") as data_file:
    f = json.load(data_file)
    data = objectpath.Tree(f)
    fnl = [f["background"][n]["name"] for n in range(len(f["background"]))]
    test = "name"
    PrettyPrinter(indent=2).pprint(list(data.execute("$.background[@.source is PHB].(" + test + ", source, skillProficiencies)")))"""

def getEntries(t, pick):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fnl = [data[t][n]["name"] for n in range(len(data[t]))]
        stuff = data[t][fnl.index(pick)]["entries"]
#        print(stuff)
#        tree = objectpath.Tree(stuff)
#        f = list(tree.execute("$"))
    return stuff

testvar = getEntries("race", "Human") + getEntries("class", "Ranger") + getEntries("background", "Acolyte")
print(testvar)

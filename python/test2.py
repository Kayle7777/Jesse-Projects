import random, json, codecs
from collections import defaultdict
from itertools import chain
#from pprint import *
#import objectpath

"""file = "data/background.json"
with codecs.open(file, "r", "utf-8-sig") as data_file:
    f = json.load(data_file)
    data = objectpath.Tree(f)
    fnl = [f["background"][n]["name"] for n in range(len(f["background"]))]
    test = "name"
    PrettyPrinter(indent=2).pprint(list(data.execute("$.background[@.source is PHB].(" + test + ", source, skillProficiencies)")))"""

def newJson(t):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fnl = [data[t][n]["name"] for n in range(len(data[t]))]
        newnl = [data[t][n]["name"] for n in range(len(data[t])) if data[t][n]["source"] == "PHB" or data[t][n]["source"] == "VGM" or data[t][n]["source"] == "XGE"]
        f = [data[t][fnl.index(n)] for n in newnl]
#        tree = objectpath.Tree(stuff)
#        f = list(tree.execute("$"))
    return f, t.title()

#newJsonRace = newJson("race")
#newJsonClass = newJson("class")
#newJsonBackground = newJson("background")

def doTheThing(a, b):
    with open("data/noUA" + a + ".json", "w") as f:
        f.write(json.dumps(b, indent=2))

#doTheThing(newJsonRace[1], newJsonRace[0])
#doTheThing(newJsonClass[1], newJsonClass[0])
#doTheThing(newJsonBackground[1], newJsonBackground[0])

import random, json, codecs
from collections import defaultdict
from itertools import chain
from pprint import *
import objectpath

file = "data/background.json"
with codecs.open(file, "r", "utf-8-sig") as data_file:
    f = json.load(data_file)
    data = objectpath.Tree(f)
    fnl = [f["background"][n]["name"] for n in range(len(f["background"]))]
    test = "name"
    PrettyPrinter(indent=2).pprint(list(data.execute("$.background[@.source is PHB].(" + test + ", source, skillProficiencies)")))

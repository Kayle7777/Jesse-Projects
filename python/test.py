import random, json, codecs
from collections import defaultdict
from itertools import chain

def roll(min, max):
    return random.randint(min,max)

def statsroller():
    diceroll = [roll(1,6),roll(1,6),roll(1,6),roll(1,6)]
    diceroll.remove(min(diceroll))
    diceroll = sum(diceroll)
    return diceroll # this is just an integer of 4d6 minus the lowest

statslist = []
for x in range(6):
    stats = ["str","dex","con","int","wis","cha"]
    n = statsroller()
    statslist.append([stats[x], n])
statslist = dict(statslist)

def rolljson(t):
    file = "data/" + t + ".json"
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        if t == "feats":
            namelist = [data[t][n]["name"] for n in range(len(data[t])) if data[t][n]["source"] == "PHB" or data[t][n]["source"] == "VGM"]
        else:
            namelist = [data[t][n]["name"] for n in range(len(data[t])) if data[t][n]["source"] == "PHB" or data[t][n]["source"] == "XGE" or data[t][n]["source"] == "VGM"]
        rtd = roll(0,len(namelist)-1)
        pick = namelist[rtd]
        return pick

racestuff = rolljson("race")
classstuff = rolljson("class")
backgroundstuff = rolljson("background")
featstuff = None
if racestuff == "Human (Variant)":
    featstuff = rolljson("feat")

def racialstats(t):
    file = "data/race.json"
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        fullnamelist = [data["race"][n]["name"] for n in range(len(data["race"]))]
        racestats = data["race"][fullnamelist.index(t)]["ability"]
        defaultd = defaultdict(list)
        if 'choose' in racestats.keys():
            p = [[k, 1] for k in racestats['choose'][0]['from']]
            random.shuffle(p)
            p = [p[x] for x in range(racestats['choose'][0]['count'])]
            if racestuff == "Half-Elf":
                p.append(['cha', 2])
            for k,v in chain(statslist.items(),dict(p).items()):
                defaultd[k].append(v)
        else:
            for k,v in chain(statslist.items(),racestats.items()):
                defaultd[k].append(v)
        fullstats = dict([(key, sum(values)) for key, values in defaultd.items()])
        return fullstats

print(statslist)
print(racialstats(racestuff))
print(str(racestuff))
print(str(classstuff))
print(str(backgroundstuff))
if featstuff != None:
    print(str(featstuff))

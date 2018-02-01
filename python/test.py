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
        namelist = [data[t][n]["name"] for n in range(len(data[t]))]
        rtd = roll(0,len(namelist)-1)
        pick = namelist[rtd]
        return [pick, rtd] # [name, number rolled (useful for using same number in json tree later)]

racestuff = rolljson("race")
classstuff = rolljson("class")
backgroundstuff = rolljson("background")

def racialstats(t):
    file = "data/race.json"
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        racestats = data["race"][racestuff[1]]["ability"]
#        if 'choose' in racestats.keys():
#            print("test")
        defaultd = defaultdict(list)
        for k,v in chain(statslist.items(),racestats.items()):
            defaultd[k].append(v)
        fullstats = dict([(key, sum(values)) for key, values in defaultd.items()])
        return fullstats

print(statslist)
print(racialstats(racestuff))
print(str(racestuff[0]))
print(str(classstuff[0]))
print(str(backgroundstuff[0]))

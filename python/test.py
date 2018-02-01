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

def rolljson(t):
    file = "data/" + t + ".json"
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        namelist = [data[t][n]["name"] for n in range(len(data[t]))]
        rtd = roll(0,len(namelist)-1)
        pick = namelist[rtd]
        racestats = data[t][rtd]["ability"]
        print(racestats)
        if 'choose' in racestats.keys():
            print("test")
#        defaultd = defaultdict(list)
#        for k,v in racestats:
#            defaultd[k].append(v)
#        defaultd = dict(defaultd);statslist2 = dict([(key, sum(values)) for key, values in defaultd.items()])

        return pick

print(rolljson("race"))





"""
def rolljson(t):
    file = "data/" + t + ".json"
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        namelist = [data[t][n]["name"] for n in range(len(data[t]))]
            if t == "races":
                a = list(data[t])
                n = roll(0,len(a)-1)
                d = data[t][a[n]]; b = list(d.keys()); c = list(d.values())
                y = [list(l) for l in zip(b, c)]
                d = [dict(statslist),dict(y)]
                defaultd = defaultdict(list)
                for k,v in chain(d[0].items(),d[1].items()):
                    defaultd[k].append(v)
                defaultd = dict(defaultd);statslist2 = dict([(key, sum(values)) for key, values in defaultd.items()])
                return [a[n], y, statslist2]
            if t == "classes":
                a = list(data[t])
                n = roll(0,len(a)-1)
                proflist = data[t][a[n]]["Proficiencies"]
                return [a[n], proflist]


print(rolljson("class"))
"""

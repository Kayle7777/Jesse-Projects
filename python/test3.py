import random, json, codecs
from collections import defaultdict
from itertools import chain

def roll(min, max):
    return random.randint(min,max)

def statsroller():
    diceroll = [roll(1,6),roll(1,6),roll(1,6),roll(1,6)]
    diceroll.remove(min(diceroll))
    diceroll = sum(diceroll)
    return diceroll

statslist = []
for x in range(6):
    stats = ["STR","DEX","CON","INT","WIS","CHA"]
    n = statsroller()
    statslist.append([stats[x], n])

file = 'rollstuff.json'

def rolljson(t):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        if t == "races":
            rpicks = []
            for x in data["races"]:
                rpicks.append(data["races"][x]["Name"])
            n = roll(0,13)
            pick = rpicks[n]
            d = data["races"][pick]; b = list(d.keys()); b.remove('Name'); c = list(d.values()); c.remove(pick)
            y = [list(l) for l in zip(b, c)]
            d = [dict(statslist),dict(y)]
            defaultd = defaultdict(list)
            for k,v in chain(d[0].items(),d[1].items()):
                defaultd[k].append(v)
            defaultd = dict(defaultd);statslist2 = dict([(key, sum(values)) for key, values in defaultd.items()])
            return [pick, y, statslist2]
        if t == "classes":
            n = roll(0,10)
            a = list(data[t])
            return a[n]

raceresult = rolljson("races") # This returns a list ['Name of race', [racial bonuses], {Statslists with racial bonuses}]
classresult = rolljson("classes")
print("You are a " + str(raceresult[0]) + " " + str(classresult) + " " + "which gives bonus racial stats: " + str(dict(raceresult[1])) + "\n\n" + "Your stat list with racial bonuses added is: " + str(raceresult[2]))
# EXAMPLE OUTPUT
#You are a Stout Halfling Cleric which gives bonus racial stats: {'DEX': 2, 'CON': 1}

#Your stat list with racial bonuses added is: {'STR': 16, 'DEX': 16, 'CON': 12, 'INT': 12, 'WIS': 10, 'CHA': 7}

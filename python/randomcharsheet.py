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

file = 'rollstuff2.json'

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
            return [pick, statslist2, y]
        if t == "classes":
            n = roll(1,11)
            n = str(n)
            return data[t][n]

raceresult = rolljson("races") # This returns a list ['Name of race', {Statslists with racial bonuses}, [racial bonuses]]
classresult = rolljson("classes")
print("Your original rolled stats were:" + "\n\n" + str(statslist) + "\n")
print("You are a " + str(raceresult[0]) + " " + str(classresult) + " " + "which gives bonus racial stats: " + str(raceresult[2]) + "\n" "Your stats with racial bonuses are:\n")
print(str(raceresult[1]))

# EXAMPLE OUTPUT
#Your original rolled stats were:

#[['STR', 14], ['DEX', 13], ['CON', 14], ['INT', 16], ['WIS', 16], ['CHA', 15]]
#
#You are a Human Sorcerer which gives bonus racial stats: [['STR', 1], ['DEX', 1], ['CON', 1], ['INT', 1], ['WIS', 1], ['CHA', 1]]
#Your stats with racial bonuses are:
#
#{'STR': 15, 'DEX': 14, 'CON': 15, 'INT': 17, 'WIS': 17, 'CHA': 16}

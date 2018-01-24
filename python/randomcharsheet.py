import random, json, codecs

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
            n = roll(1,14)
            pick = rpicks[n]
            return(pick)
        if t == "classes":
            n = roll(1,11)
            n = str(n)
            return data[t][n]

raceresult = rolljson("races")
classresult = rolljson("classes")

print("You are a " + str(raceresult) + " " + str(classresult) + "!" + " " + "Your stats are:\n")
print(statslist)

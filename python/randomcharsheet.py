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
    number = statsroller()
    statslist.append([stats[x], number])

file = 'rollstuff.json'

def rolljson(thing,min,max):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        n = roll(min,max)
        return data[str(thing)][str(n)]

classresult = rolljson("classes",1,11)
raceresult = rolljson("races",1,14)

print(statslist[0])
if str(classresult) == "Mountain Dwarf" or str(classresult) == "Half-Orc" or str(classresult) "Dragonborn":
    statslist[0][1] = statslist[0][1] + 2
elif str(classresult) == "Human":
    statslist[0][1] = statslist[0][1] + 1

print("You are a " + str(raceresult) + " " + str(classresult) + "!" + " " + "Your stats are:\n")
print(statslist)

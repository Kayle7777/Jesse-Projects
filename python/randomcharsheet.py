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

#def rolljson(thing,min,max):
#    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
#        data = json.load(data_file)
#        n = roll(min,max)
#        return data[str(thing)][str(n)]

def rolljson(thing):
    thing = str(thing)
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        if thing == "races":
            rpicks = []
            for x in data[thing]:
                rpicks.append(data[thing][x])
                n = roll(1,14)
            pick = rpicks[n]
            return(pick)
        if thing == "classes":
            n = roll(1,11)
            return data(str["classes"][str(n)]

classresult = rolljson(classes)
raceresult = rolljson(races)

print("You are a " + str(raceresult) + " " + str(classresult) + "!" + " " + "Your stats are:\n")
print(statslist)

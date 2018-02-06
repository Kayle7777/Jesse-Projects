import random, json, codecs
from collections import defaultdict
from itertools import chain

def dictchain(adict, bdict):
    defaultd = defaultdict(list)
    for k,v in chain(dict(adict).items(),dict(bdict).items()):
        defaultd[k].append(v)
    return defaultd

def roll(min, max):
    return random.randint(min,max)

def statsroller():
    diceroll = [roll(1,6),roll(1,6),roll(1,6),roll(1,6)]
    diceroll.remove(min(diceroll))
    diceroll = sum(diceroll)
    return diceroll # this is just an integer of 4d6 minus the lowest

def getprofs(t, pick):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fullnamelist = [data[t][n]["name"] for n in range(len(data[t]))]
        profs = []
        if t == "race":
            raceSkillData = data["race"][fullnamelist.index(pick)]
            if "proficiency" in raceSkillData:
                profs.append(raceSkillData["proficiency"])
        if t == "class":
            classSkillData = data["class"][fullnamelist.index(pick)]["startingProficiencies"]["skills"]
            if "choose" in classSkillData:
                profchoices = classSkillData["from"]
                random.shuffle(profchoices)
                profchoices = [profchoices[x] for x in range(classSkillData["choose"])]
                profs.extend(profchoices)
            else:
                profs.extend(data[t][fullnamelist.index(pick)]["startingProficiencies"])
            savingThrowData = [data["class"][fullnamelist.index(pick)]["proficiency"][x].title() + " Saving Throws" for x in range(2)]
            profs.extend(savingThrowData)
        if t == "background":
            backgroundSkillData = data[t][fullnamelist.index(pick)]["skillProficiencies"]
            profs.append(backgroundSkillData)
        return profs


def rolljson(t):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        if t == "feats":
            namelist = [data[t][n]["name"] for n in range(len(data[t])) if data[t][n]["source"] == "PHB" or data[t][n]["source"] == "VGM"]
        else:
            namelist = [data[t][n]["name"] for n in range(len(data[t])) if data[t][n]["source"] == "PHB" or data[t][n]["source"] == "XGE" or data[t][n]["source"] == "VGM"]
        rtd = roll(0,len(namelist)-1)
        pick = namelist[rtd]
        return pick

def racialstats(t):
    file = "data/race.json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fullnamelist = [data["race"][n]["name"] for n in range(len(data["race"]))]
        racestats = data["race"][fullnamelist.index(t)]["ability"]
        defaultd = defaultdict(list)
        if "choose" in racestats.keys():
            racestats = [[k, 1] for k in racestats["choose"][0]["from"]]
            random.shuffle(racestats)
            racestats = [racestats[x] for x in range(data["race"][fullnamelist.index(t)]["ability"]["choose"][0]["count"])]
            if racestuff == "Half-Elf":
                racestats.append(["cha", 2])
        fullstats = dict([(key, sum(values)) for key, values in dictchain(statslist, racestats).items()])
        return fullstats

statslist = []
for x in range(6):
    stats = ["str","dex","con","int","wis","cha"]
    n = statsroller()
    statslist.append([stats[x], n])
statslist = dict(statslist)

racestuff = rolljson("race")
classstuff = rolljson("class")
backgroundstuff = rolljson("background")

sumProfs = [getprofs("background", backgroundstuff), getprofs("class", classstuff)]
if getprofs("race", racestuff) != []:
    sumProfs.append(getprofs("race", racestuff))

featstuff = None
if racestuff == "Human (Variant)":
    checkprofs = ["Human", classstuff, backgroundstuff];checkprofs.extend(sumProfs)
    print(checkprofs)
    featstuff = rolljson("feat")


print(str(statslist) + "\n"
+ str(racialstats(racestuff)) + "\n"
+ str(racestuff) + "\n"
+ str(classstuff) + "\n"
+ str(backgroundstuff) + "\n"
+ str(sumProfs))

if featstuff != None:
    print(str(featstuff))

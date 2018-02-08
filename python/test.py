import random, json, codecs
from collections import defaultdict
from itertools import chain

def dictChain(adict, bdict):
    defaultd = defaultdict(list)
    for k,v in chain(dict(adict).items(),dict(bdict).items()):
        defaultd[k].append(v)
    return defaultd

def roll(min, max):
    return random.randint(min,max)

def statsRoller():
    diceroll = [roll(1,6),roll(1,6),roll(1,6),roll(1,6)]
    diceroll.remove(min(diceroll))
    diceroll = sum(diceroll)
    return diceroll # this is just an integer of 4d6 minus the lowest

def listShuffler(data, count):
    random.shuffle(data)
    data = [data[x] for x in range(count)]
    return data

def inList(list1, list2):
    inlist = [x for x in list2 if x in list1]
    return inlist

def getProfs(t, pick):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        profs = []
        fullnamelist = [data[t][n]["name"] for n in range(len(data[t]))]
        if t == "race":
            raceSkillData = data["race"][fullnamelist.index(pick)]
            if "proficiency" in raceSkillData:
                profs.append(raceSkillData["proficiency"])
        if t == "class":
            classSkillData = data["class"][fullnamelist.index(pick)]["startingProficiencies"]["skills"]
            if "choose" in classSkillData:
                profs.extend(listShuffler(classSkillData["from"], classSkillData["choose"]))
            else:
                profs.extend(data[t][fullnamelist.index(pick)]["startingProficiencies"])
            savingThrowData = [data["class"][fullnamelist.index(pick)]["proficiency"][x].title() + " Saving Throws" for x in range(2)]
            profs.extend(savingThrowData)
        if t == "background":
            backgroundSkillData = data[t][fullnamelist.index(pick)]["skillProficiencies"]
            profs.append(backgroundSkillData)
        return profs

def rollJson(t):
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

def racialStats(t):
    file = "data/race.json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fullnamelist = [data["race"][n]["name"] for n in range(len(data["race"]))]
        racestats = data["race"][fullnamelist.index(t)]["ability"]
        if "choose" in racestats.keys():
            racestats = listShuffler([[k, 1] for k in racestats["choose"][0]["from"]], data["race"][fullnamelist.index(t)]["ability"]["choose"][0]["count"])
            if raceStuff == "Half-Elf":
                racestats.append(["cha", 2])
        fullstats = {key: sum(values) for (key, values) in dictChain(statslist, racestats).items()}
        return fullstats

statslist = {x: statsRoller() for x in ["str","dex","con","int","wis","cha"]}

raceStuff = rollJson("race")
classStuff = rollJson("class")
backgroundStuff = rollJson("background")

sumProfs = [getProfs("background", backgroundStuff) + getProfs("class", classStuff)]
if getProfs("race", raceStuff) != []:
    sumProfs.append(getProfs("race", raceStuff))

featStuff = None
if raceStuff == "Human (Variant)":
#    checkProfs = ["Human", classStuff, backgroundStuff];checkProfs.extend(sumProfs)
#    print(checkProfs)
    featStuff = rollJson("feat")


print(str(statslist) + "\n"
+ str(racialStats(raceStuff)) + "\n"
+ str(raceStuff) + "\n"
+ str(classStuff) + "\n"
+ str(backgroundStuff) + "\n"
+ str(sumProfs))

if featStuff != None:
    print(str(featStuff))

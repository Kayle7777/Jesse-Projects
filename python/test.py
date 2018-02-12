import random, json, codecs
from collections import defaultdict
from itertools import chain
from pprint import *
import objectpath

def dictChain(adict, bdict):
    defaultd = defaultdict(list)
    for k,v in chain(dict(adict).items(),dict(bdict).items()):
        defaultd[k].append(v)
    return defaultd

def statsRoller():
    diceroll = [random.randint(1,6) for x in range(4)]
    diceroll.remove(min(diceroll))
    return sum(diceroll) # this is just an integer of 4d6 minus the lowest

def listShuffler(data, count):
    random.shuffle(data)
    data = [data[x] for x in range(count)]
    return data

def getStuff(t, pick):
    file = "data/" + t + ".json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        profs = []
        entries = []
        fnl = [data[t][n]["name"] for n in range(len(data[t]))]
        if t == "race":
            raceSkillData = data["race"][fnl.index(pick)]
            entries.append(raceSkillData["entries"])
            if "proficiency" in raceSkillData:
                profs.append(raceSkillData["proficiency"])
        if t == "class":
            classStuff = data["class"][fnl.index(pick)]
            classSkillData = classStuff["startingProficiencies"]["skills"]
            if "choose" in classSkillData:
                profs.extend(listShuffler(classSkillData["from"], classSkillData["choose"]))
            else:
                profs.extend(data[t][fnl.index(pick)]["startingProficiencies"])
            savingThrowData = [data["class"][fnl.index(pick)]["proficiency"][x].title() + " Saving Throws" for x in range(2)]
            profs.extend(savingThrowData)
        if t == "background":
            backgroundSkillData = data[t][fnl.index(pick)]["skillProficiencies"]
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
        rtd = random.randint(0,len(namelist)-1)
        pick = namelist[rtd]
        return pick

def racialStats(t):
    file = "data/race.json"
    with codecs.open(file, "r", "utf-8-sig") as data_file:
        data = json.load(data_file)
        fnl = [data["race"][n]["name"] for n in range(len(data["race"]))]
        racestats = data["race"][fnl.index(t)]["ability"]
        if "choose" in racestats.keys():
            racestats = listShuffler([[k, 1] for k in racestats["choose"][0]["from"]], data["race"][fnl.index(t)]["ability"]["choose"][0]["count"])
            if raceStuff == "Half-Elf":
                racestats.append(["cha", 2])
        fullstats = {key: sum(values) for (key, values) in dictChain(statslist, racestats).items()}
        return [fullstats, racestats]

statslist = {x: statsRoller() for x in ["str","dex","con","int","wis","cha"]}

raceStuff = rollJson("race")
classStuff = rollJson("class")
backgroundStuff = rollJson("background")

#sumProfs = [getStuff("background", backgroundStuff) + getStuff("class", classStuff)]
#if getStuff("race", raceStuff) != []:
#    sumProfs.append(getStuff("race", raceStuff))

featStuff = None
if raceStuff == "Human (Variant)":
#    checkProfs = ["Human", classStuff, backgroundStuff];checkProfs.extend(sumProfs)
#    print(checkProfs)
    featStuff = rollJson("feat")

jsonPush = {}
jsonPush ["Stats"] = {
#"beforeRaceBonus": statslist,
"afterRaceBonus": racialStats(raceStuff)[0]
}
jsonPush ["Race"] = {
"name": raceStuff,
"statsBonus": racialStats(raceStuff)[1],
"raceProficiencies": getStuff("race", raceStuff)
}
jsonPush ["Class"] = {
"name": classStuff,
"subclass": None,
"classProficiencies": getStuff("class", classStuff)
}
jsonPush ["Background"] = {
"name": backgroundStuff,
"backgroundProficiencies": getStuff("background", backgroundStuff)
}

if featStuff != None:
    jsonPush ["Feat"] = {
    "name": featStuff
    }

#PrettyPrinter(indent=2).pprint(jsonPush)

with open("sheets/" + raceStuff + " " + classStuff + " " + backgroundStuff + ".json", "w") as f:
    f.write(json.dumps(jsonPush, indent=2))

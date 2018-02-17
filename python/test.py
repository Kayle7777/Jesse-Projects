import random, json, codecs
from testFunctions import *

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

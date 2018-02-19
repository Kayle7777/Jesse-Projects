import random, json, codecs
from testFunctions import listShuffler

class CharacterSheet:
    "For learning"

    def __init__(self, t):

        self.file = "data/" + t + ".json"
        self.filename = t
        self.data = json.load(codecs.open(self.file, "r", "utf-8-sig"))

        with codecs.open(self.file, "r", "utf-8-sig") as data_file:

            self.namelist = [self.data[t][n]["name"] for n in range(len(self.data[t])) if self.data[t][n]["source"] == "PHB" or self.data[t][n]["source"] == "XGE" or self.data[t][n]["source"] == "VGM"]
            rtd = random.randint(0,len(self.namelist)-1)
            self.name = self.namelist[rtd]
            self.fullnamelist = [self.data[t][n]["name"] for n in range(len(self.data[t]))]
            self.number = self.fullnamelist.index(self.name)
            return

    def getStuff(self):
        with codecs.open(self.file, "r", "utf-8-sig") as data_file:
            self.profs = []
            if self.filename == "race":
                raceSkillData = self.data["race"][self.fullnamelist.index(self.name)]
                if "proficiency" in raceSkillData:
                    self.profs.append(raceSkillData["proficiency"])
            if self.filename == "class":
                classSkillData = self.data["class"][self.fullnamelist.index(self.name)]["startingProficiencies"]["skills"]
                if "choose" in classSkillData:
                    self.profs.extend(listShuffler(classSkillData["from"], classSkillData["choose"]))
                else:
                    self.profs.extend(self.data[self.filename][self.fullnamelist.index(self.name)]["startingProficiencies"])
                self.profs.extend([self.data["class"][self.fullnamelist.index(self.name)]["proficiency"][x].title() + " Saving Throws" for x in range(2)])
            if self.filename == "background":
                self.profs.append(self.data[self.filename][self.fullnamelist.index(self.name)]["skillProficiencies"])
            return self.profs

testrace = CharacterSheet("race")
testclass = CharacterSheet("class")
testbackground = CharacterSheet("background")
proficiencies = testrace.getStuff() + testclass.getStuff() + testbackground.getStuff()
print(testclass.name)
print(proficiencies)

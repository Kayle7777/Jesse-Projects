import codecs,random,json

file="rollstuff.json"

def roll(min, max):
    return random.randint(min,max)

def rollrace():
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        rpicks = []
        for x in data["races"]:
            rpicks.append(data["races"][x])
        n = roll(1,14)
        pick = rpicks[n]
        return(pick)
print(rollrace())

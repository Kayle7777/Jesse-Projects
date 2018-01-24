import codecs,random,json

file = 'rollstuff2.json'

def roll(min, max):
    return random.randint(min,max)

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
print(rolljson("races"))
print(rolljson("classes"))

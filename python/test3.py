import codecs,random,json

file = 'rollstuff2.json'

def roll(min, max):
    return random.randint(min,max)


statslist = [['STR', 8], ['DEX', 11], ['CON', 12], ['INT', 14], ['WIS', 12], ['CHA', 12]]
print(statslist)
def rolljson(t):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        if t == "races":
            rpicks = []
            for x in data["races"]:
                rpicks.append(data["races"][x]["Name"])
            n = roll(0,13)
            pick = rpicks[n]
            d = data["races"][pick]; b = list(d.keys()); b.remove('Name'); c = list(d.values()); c.remove(pick)
            y = [list(l) for l in zip(b, c)]
            print(y)
            for x in range(6):
                statslist[x][1] + y[x][1]
            return(pick)
        if t == "classes":
            n = roll(1,11)
            n = str(n)
            return data[t][n]
print(rolljson("races"))
print(rolljson("classes"))
print(statslist)

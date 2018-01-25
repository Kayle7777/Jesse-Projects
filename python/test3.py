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
            n = roll(0,13)
            pick = rpicks[n]
            def racialstats():
                d = data["races"][pick]
                b = list(d.keys())
                c = list(d.values())
                del b[0]
                del c[0]
                y = [list(l) for l in zip(b, c)]
                pstats = print(y)
                return pstats
            pstats = racialstats()
            p = [pick,pstats]
            return(p)
        if t == "classes":
            n = roll(1,11)
            n = str(n)
            return data[t][n]

print(rolljson("races"))
print(rolljson("classes"))

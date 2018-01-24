import codecs,random,json

<<<<<<< HEAD
file="rollstuff2.json"
=======
file = 'rollstuff2.json'
>>>>>>> 73594d3359a6e85cbca5e5aae20c759de8467b44

def roll(min, max):
    return random.randint(min,max)

def rolljson(t):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
<<<<<<< HEAD
        rpicks = []
        for x in data["races"]:
            rpicks.append(data["races"][x]["Name"])
        n = roll(1,14)
        pick = rpicks[n]
        return(pick)
print(rollrace())
=======
        if t == "races":
            rpicks = []
            for x in data["races"]:
                rpicks.append(data["races"][x])
            n = roll(1,14)
            pick = rpicks[n]
            return(pick)
print(rolljson("races"))
>>>>>>> 73594d3359a6e85cbca5e5aae20c759de8467b44

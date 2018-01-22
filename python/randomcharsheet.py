import random, json, codecs

def roll(min, max):
    return random.randint(min,max)

file = 'C:\\Users\\Jesse\\Desktop\\projects\\python\\rollstuff.json'

def rollclass(thing):
    with codecs.open(file, 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
        n = roll(1,11)
        return data[str(thing)][str(n)]
classresult = rollclass("classes")

print("Your class is " + str(classresult) + "!")

import random, json
import jsonwriter as jw

def randomizer(min, max):
    return random.randint(min,max)
print(randomizer(1,6))

print(jw.jsonwriter('C:\\classes.json','class','name'))

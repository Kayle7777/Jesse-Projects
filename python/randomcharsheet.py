import random, json
import jsonwriter as jw


def roll(min, max):
    return random.randint(min,max)
print(roll(1,6))

stuff = jw.jw('C:\\classes.json','class','name')

print(stuff)

import random, json
import jsonwriter as jw

def r(min, max):
    return random.randint(min,max)
print(r(1,6))

print(jw.jw('C:\\classes.json','class','name'))

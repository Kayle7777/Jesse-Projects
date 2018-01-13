import json

data = {'ObjectInterpolator': 1629,  'PointInterpolator': 1675, 'RectangleInterpolator': 2042}

d = {"class":"name",
     "children":[{'name':k,"size":v} for k,v in data.items()]}

j = json.dumps(d, indent=4)

f = open('sample.json', 'w')

f.write(j)

f.close()

from urllib.request import urlopen
import json
u = urlopen('https://5etools.com/classes.html')
resp = json.loads(u.read())
from pprint import pprint
pprint(resp)

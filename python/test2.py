import random, json, codecs
from collections import defaultdict
from itertools import chain

def randomListSum(n, total):
    randomNumbers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(randomNumbers + [total], [0] + randomNumbers)]

print(randomListSum(5, 100))

import random

def randomListSum(n, total):
    randomNumbers = sorted(random.sample(range(1, total), n - 1))
    x = [a - b for a, b in zip(randomNumbers + [total], [0] + randomNumbers)]
    return x

print(randomListSum(5, 100))

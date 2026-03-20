import random

def roll(count, sides):
    total = 0
    for i in range(count):
        total += random.randint(1, sides)
    return total

def roll20(advantage=False, disadvantage=False):
    if advantage and disadvantage:
        return random.randint(1, 20)
    elif advantage:
        return max(random.randint(1, 20), random.randint(1, 20))
    elif disadvantage:
        return min(random.randint(1, 20), random.randint(1, 20))
    else:
        return random.randint(1, 20)


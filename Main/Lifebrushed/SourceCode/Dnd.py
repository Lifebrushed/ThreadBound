import random

def d20(advantage=False, disadvantage=False):
    roll = random.randint(1, 20)

    if advantage and disadvantage:
        return roll

    if advantage:
        return max(roll, random.randint(1,20))

    if disadvantage:
        return min(roll, random.randint(1,20))

    return roll

def dbase(count=1, sides=4) :
    roll = random.randint(1, sides) * count
    return roll

def d4(count=1):
    return dbase(count, 4)

def d6(count=1):
    return dbase(count, 6)

def d8(count=1):
    return dbase(count, 8)

def d10(count=1):
    return dbase(count, 10)

def d12(count=1):
    return dbase(count, 12)

def d100(count=1):
    return dbase(count, 100)

def check(req=1, inputs=20):
    if inputs >= req :
        return True
    else :
        return False


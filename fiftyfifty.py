from random import randint

def fifty_fifty(amount):
    rolls = 0
    ones = 0
    twos = 0
    while rolls < amount:
        roll = randint(1, 2)
        if roll == 1:
            ones += 1
        elif roll == 2:
            twos += 1
        rolls += 1
    print(f"Ener: {ones} Toer: {twos}")
        
fifty_fifty(1000)
fifty_fifty(1000)
fifty_fifty(1000)
fifty_fifty(1000)
fifty_fifty(1000)
fifty_fifty(1000)
fifty_fifty(1000)

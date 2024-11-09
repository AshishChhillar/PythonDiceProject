import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll_dice = random.randint (min_value, max_value)
    return roll_dice
value = roll_dice()
print(value)
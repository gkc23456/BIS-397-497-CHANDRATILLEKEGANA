import random

def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    die3 = random.randrange(1, 7)
    die4 = random.randrange(1, 7)
    die5 = random.randrange(1, 7)
    return (die1, die2, die3, die4, die5)

def display_dice(dice):
    die1, die2, die3, die4, die5 = dice
    print(f'{die1} {die2} {die3} {die4} {die5}')
    
die_values = roll_dice()
display_dice(die_values)    

for i in range(3):
    value = int(input('Enter which die to roll (-99 to break): '))
        
    if value == -99:
        break
    else:
        roll_dice():
    
        def display_dice(dice):
        die1, die2, die3, die4, die5 = dice
        print(f'{die1} {die2} {die3} {die4} {die5}')
    
        die_values = roll_dice()
        display_dice(die_values)
    
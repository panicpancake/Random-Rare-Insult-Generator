#! python3
#Random Rare Insult Generator
#Author: panic
import random
adjectives = []
insults = []
adj=' '
ins=' '
with open('D:/Programs/Adjectives.txt') as inputfile:
    for line in inputfile:
        adjectives.append(line.strip().split(','))
with open('D:/Programs/Insults.txt') as inputfile:
    for line in inputfile:
        insults.append(line.strip().split(','))
adj=str(adjectives[random.randint(0,25)])
ins=str(insults[random.randint(0,25)])
print('You ' + adj.strip('[',).strip(']').strip(" ' ") + ' ' + ins.strip('[',).strip(']').strip(" ' "))



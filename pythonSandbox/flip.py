import random
#----------------------------------------------------------------------
def flip(numFlips):
    """returns ratio of 'heads'/total bi-side simulated flips
    'heads' defined as float < 0.5 from random float >0<1"""
    heads = 0.0
    for i in range(numFlips):
        if random.random()<0.5:
            heads += 1
    return heads/numFlips
    
#----------------------------------------------------------------------
def flipSim(numFlipsPerTrial,numTrials):
    """returns the mean of a sample pool of binomial 'flips' from random pool >0<1"""
    ratioHeads = []
    for i in range(numTrials):
        ratioHeads.append(flip(numFlipsPerTrial))
    mean = sum(ratioHeads)/len(ratioHeads)
    return mean
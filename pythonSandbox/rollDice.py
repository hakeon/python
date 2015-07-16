import random

#----------------------------------------------------------------------
def rollDie():
    """return a random int > 0 < 7"""
    return random.choice([1,2,3,4,5,6])

#----------------------------------------------------------------------
def rollN(n):
    """rolls the die for the rollDie function for 'n' times"""
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print result
    
    
#----------------------------------------------------------------------
def findExtremeDivisors(n1,n2):
    """
    assumes n1 and n2 are positive int
    returns a tuple with the minimum and maximum common divisors
    """
    divisors = () # an inital empty tuple
    minDiv, maxDiv = None, None
    
    for i in range(2, min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0:
            if minDiv == None or i < minDiv:
                minDiv = i
            if maxDiv == None or i > maxDiv:
                maxDiv = i
    print (minDiv,maxDiv)
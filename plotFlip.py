import random
#----------------------------------------------------------------------
def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
       Plots results of 2**minExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    
    pylab.title('Difference Between Heads & Tails')
    pylab.xlable('Number of Flips')
    pylab.ylable('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlable('Number of Flips')
    pylab.ylable('#Heads/#Tails')
    pylab.plot(xAxis, ratios)
    
random.seed(0)
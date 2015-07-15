def findDivisors(n1,n2):
    '''
    Assumes n1 and n2 are positive ints
    Return a tuple of all common divisors
    '''
    divisors = () # the initial emply tuple
    for i in range(1, min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    print divisors
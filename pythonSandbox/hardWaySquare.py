# To square an integer the hard way.
x = int(raw_input('Please pick a number. '))
ans = 0
iterateLeft = x

while(iterateLeft != 0):
    ans = ans + x
    iterateLeft = iterateLeft - 1
print str(x)+'*'+str(x)+'='+str(ans)

import pylab

principle = raw_input("How much do you want to deposit? ")
interestRate = raw_input("What is the interest rate? ")
term = raw_input("For how many years will you invest? ")
values = []

principle = float(principle)
interestRate = float(interestRate)
term = int(term)

for i in range(term+1):
    values.append(principle)
    principle += principle*interestRate
pylab.plot(values,'ro')
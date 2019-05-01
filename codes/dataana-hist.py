import numpy as np
from momentoHist import momentoHist

mu = 5
sg = 1
nbins = 100
res = 10.

hist = []

s = np.random.normal(mu, sg, 10000)
[hist.append(0) for i in range(nbins)]

for i in s:
    hist[ int(i*res) ] += 1
    
mt = momentoHist()
mt.momento1(hist)

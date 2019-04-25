import numpy as np
from momento import momento

outDistData = open("datafile.dat", "w")

mu = 5
sg = 1
nbins = 100
res = 10.

hist = []

s = np.random.normal(mu, sg, 10000)
[hist.append(0) for i in range(nbins)]

for i in s:
    hist[ int(i*res) ] += 1
    
for j in range(nbins):
#    print hist[j]
    outDistData.write('%0.2f %d\n' % (j/res, hist[j]))

inData = open ("datafile.dat", "r") # Reading file
data = inData.readlines() 

mt = momento()
mt.prube(data)
mt.moment()
mt.average()

import numpy as np


# Distribution Parameters
mu = 5
sg = 1
nevents = 10000


# Histogram parameters
hist = [] # Array for histogram
startBin = 0.
endBin = 10.
nbins = 100

binwidth = (endBin - startBin) / nbins
[hist.append(0) for i in range(nbins)] # Inizialiting histo

# Creating distribution 
s = np.random.normal(mu, sg, nevents)

tmp = []
[tmp.append(np.random.normal(mu, sg, nevents)) for i in range(10)]


[print(tmp[0][i]) for i in range(nevents)]


# Filling histogram
for i in s:
    hist[ int(i/binwidth) ] += 1


# Saving histogram into file
outDistData = open( "datafile.dat", "w" )
outDistData.write( "# startBin %0.1f endBin %0.1f nbins %d\n" % (startBin, endBin, nbins))
for j in range( nbins ):
    outDistData.write('%0.2f %d\n' % (j*binwidth, hist[j]))
outDistData.close()

print("bye")

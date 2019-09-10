from momento import momento
from numpy import loadtxt


# Reading data from file
#inData = open ("datafile.dat", "r")
inData = loadtxt("datafile.dat")

# Calculating moments
mt = momento()
#a = mt.momento1(inData)
a = mt.momento2(inData)
print( "First moment is:", a )

from momento import momento


# Reading data from file
inData = open ("datafile.dat", "r")


# Calculating moments
mt = momento()
a = mt.momento1(inData)
print( "First moment is:", a )

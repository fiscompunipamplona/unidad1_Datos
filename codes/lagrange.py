from numpy import loadtxt, array
from scipy import linspace
from scipy.interpolate import interp1d
from inteLagrange import inteLagrange

inter = inteLagrange()

outInteData = open("interData.dat", "w")

a = loadtxt("../data/neutron-resonant.dat", float)
n = 9 # Polonomial order
x = 0.
y = 0.

for k in range( 1000 ):
    x = k*0.2
    y = inter.inter( a, n, x )
    outInteData.write('%0.1f %0.1f\n' % (x, y))

outInteData.close()

new_x = linspace( min(a[:,0]), max(a[:,0]), 1000)
new_y = interp1d(a[:,0], a[:,1], kind='cubic')(new_x)

#outSpline = open( "interSpline.dat", "w" )

#for i in range( len(new_y) ):
#    outSpline.write('%0.1f %0.1f\n' % (new_x[i], new_y[i]) )

#outSpline.close()

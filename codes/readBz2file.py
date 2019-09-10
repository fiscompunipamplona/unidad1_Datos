import bz2

n = 0

with bz2.open( input ("Please, enter the filename: "), "rt" ) as bz_file:
     for line in bz_file:
        rline = line.rstrip('\n').split(' ')
        print( rline[0] )
        n += 1
        if n == 60:
            break

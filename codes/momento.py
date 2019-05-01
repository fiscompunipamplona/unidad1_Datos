class momento:
    
    m1 = 0.
    N = 0

    def __init__(self):
        self.m1 = 0.
        self.N = 0

    def momento1(self, dfile):
        for i in dfile:
            columns = i.split(" ")
            if columns[0] != "#":
                bin_i = float( columns[0] )
                freq = float( columns[1] )
                self.N += freq
                self.m1 += bin_i * freq

        self.m1 /= self.N
        return ( self.m1 )

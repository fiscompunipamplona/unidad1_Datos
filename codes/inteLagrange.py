class inteLagrange:

    y = 0.
    ld = 0.

    def __init__(self):
        self.y = 0.
        self.ld = 0.

    def inter(self, data, nor, x):
        self.y = 0.
        for i in range( nor ):
            self.ld = 1.
            for j in range( nor ):
                if i != j:
                    self.ld *= (x-data[j,0]) / (data[i,0]-data[j,0])
            self.y += data[i,1]*self.ld

        return (self.y)

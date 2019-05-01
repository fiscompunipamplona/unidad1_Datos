
class momentoHist:
    
    m1 = 0.
    N = 0

    def __init__(self):
        self.m1 = 0.
        self.N = 0

    def momento1(self, freq):
        for i in freq:
            self.N += i
        for j in range( len(freq) ):
            self.m1 += (j/10.)*freq[j]

        print("N = ", self.N, "; m1 = ", self.m1/self.N)

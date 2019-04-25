
class momento:
    
    y = []

    def __init__(self):
        print "hi"

    def prube(self, dafi):
        for i in dafi:
            xy = i.split()
            self.y.append( xy[1] )

    def moment(self):
        for i in range (len(self.y)):
            print self.y[i]

    def average(self):
        print "hi00"

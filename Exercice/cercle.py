"""
 classe Cercle permettant de créer un cercle C(O,r) de centre O(a,b) et de rayon r
"""
class cercle():
    def __init__(self, a,b,r):
        self.a = a
        self.b = b
        self.r = r
    def surface(self):
        return 3.14*(self.r)**2
    
    def perimetre(self):
        return 6.28*self.r
    
    def testAppartenance(self,x,y): 
        cond = ((((x - self.a)**2) + ((y - self.b)**2))==(self.r)**2)
        return "yes" if cond else "no"
# instanciation
v = cercle(0,0,5)
print(v.surface(),"---",v.perimetre())
print(v.testAppartenance(0,5))

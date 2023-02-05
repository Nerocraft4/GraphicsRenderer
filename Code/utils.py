import numpy as np

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.c = [x,y,z]
    def get(self):
        return self.c

class Segment:
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.col = color

class Vector:
    def __init__(self, pt, og=Point(0,0)):
        self.x = pt.x - og.x
        self.y = pt.y - og.y
        self.z = pt.z - og.z
        self.c = [self.x, self.y, self.z]
    def get(self):
        return self.c
    def norma(self):
        return np.sqrt(np.sum([vi*vi for vi in self.c]))
    def norml(self):
        n = self.norma()
        v = [round(vi/n,5) for vi in self.c]
        return Vector(Point(v[0],v[1],v[2]))
    def rotate(self, alpha):
        ux = self.x*np.cos(alpha)-self.y*np.sin(alpha)
        uy = self.y*np.cos(alpha)+self.x*np.sin(alpha)
        return Vector(Point(ux, uy, self.z))
    def pprod(self, other):
        v = self.c
        u = other.c
        l = np.sum([v[i]*u[i] for i in range(3)])
        return l
    def xprod(self, other):
        v = self.c
        u = other.c
        w = [v[1]*u[2]-v[2]*u[1],v[2]*u[0]-v[0]*u[2],v[0]*u[1]-v[1]*u[0]]
        return Vector(Point(w[0],w[1],w[2]))

#should we define a raycast class?
def rycst(og, vd, mu):
    return np.add(og, [vdi*mu for vdi in vd])

import numpy as np
from graphics import *

TOL = 0.02
DIM = 500
SCL = 100

charmap = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
simple_charmap = "@%#*+=-:. "

class Punt:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.c = [x,y,z]
    def get(self):
        return self.c
    def getcd(self):
        x = self.x*SCL + DIM/2
        y = DIM/2 - self.y*SCL
        return Point(x, y)

class Segment:
    def __init__(self, a, b, color='red', width=1):
        self.name = "Segment"
        self.a = a
        self.b = b
        self.col = color
        self.w = width
    def get(self):
        return self.a.get(),self.b.get()
    def draw_segment(self):
        line = Line(self.a.getcd(), self.b.getcd())
        line.setOutline(self.col)
        line.setWidth(self.w)
        return line
    def contains(self, p):
        ab = Vector(self.a,self.b)
        pa = Vector(p,self.a)
        pb = Vector(p,self.b)
        dnorm2 = pa.xprod(pb).norma()
        if dnorm2 < TOL:
            dnorm1 = np.abs(ab.norma()-(pa.norma()+pb.norma()))
            if dnorm1 < TOL*TOL:
                return True, ab
        return False, None

class Plane:
    def __init__(self, vertices, color='red'):
        #check vertices "planarity"
        if len(vertices)>3:
            v0 = Vector(vertices[1], vertices[0])
            v1 = Vector(vertices[2], vertices[0])
            v0x1 = v0.xprod(v1)
            for i in range(3,len(vertices)):
                v2 = Vector(vertices[i], vertices[0])
                v0x2 = v0.xprod(v2)
                v3 = v0x1.xprod(v0x2)
                print(v3.get(),v3.norma())
                if v3.norma()>TOL:
                    print("Can't create plane, points aren't coplanar")
                    return None
        self.name = "Plane"
        self.vertices = vertices
        v0 = Vector(self.vertices[1], self.vertices[0])
        v1 = Vector(self.vertices[2], self.vertices[1])
        self.normal = v0.xprod(v1)
        self.col = color
    def get(self):
        return self.vertices
    def contains(self, p):
        v0 = Vector(p, self.vertices[0])
        v1 = Vector(p, self.vertices[1])
        v0x1 = v0.xprod(v1)
        v0x2 = self.normal
        v3 = v0x1.xprod(v0x2)
        if v3.norma()>TOL:
            return False, None
        else:
            return True, self.normal

class Vector:
    def __init__(self, pt, og=Punt(0,0,0)):
        self.dx = 0.05
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
        return Vector(Punt(v[0],v[1],v[2]))
    def rycst(self, org, length, world):
        cc = 0
        dx = 0.01
        while cc<length:
            endpoint = Punt(org.x+self.x*cc,org.y+self.y*cc,org.z+self.z*cc)
            for element in world:
                col, seg = element.contains(endpoint)
                if col:
                    deg = self.degrr(seg)
                    return endpoint, element.name, deg*cc/length
            cc+=dx
        return endpoint, None, 0
    def rtate(self, alpha):
        ux = self.x*np.cos(alpha)-self.y*np.sin(alpha)
        uy = self.y*np.cos(alpha)+self.x*np.sin(alpha)
        return Vector(Punt(ux, uy, self.z))
    def pprod(self, other):
        v = self.c
        u = other.c
        l = np.sum([v[i]*u[i] for i in range(3)])
        return l
    def xprod(self, other):
        v = self.c
        u = other.c
        w = [v[1]*u[2]-v[2]*u[1],v[2]*u[0]-v[0]*u[2],v[0]*u[1]-v[1]*u[0]]
        return Vector(Punt(w[0],w[1],w[2]))
    def degrr(self, other):
        n1 = self.norma()
        n2 = other.norma()
        return ((self.xprod(other).norma()/(n1*n2)))

colors = ['red','blue','green','pink','brown']
world = []

#superficie 1
# B = Punt(0,0,0)
# C = Punt(0.58,0.58,0.58)
# D = Punt(0.71,-0.71,0)
# E = Punt(1.28,-0.13,0.58)
# F = Punt(0.32,0.32,-0.89)
# G = Punt(0.9,0.9,-0.32)
# H = Punt(1.03,-0.39,-0.89)
# C1 = Plane([B,C,E,D])
# world.append(C1)
# C2 = Plane([B,C,G,F])
# world.append(C2)
# C3 = Plane([B,F,H,D])
# world.append(C3)

P1 = Punt(0,0,0)
P2 = Punt(0,0,2)
P3 = Punt(0,-1,2)
P4 = Punt(0,-1,0)
CP = Plane([P1,P2,P3,P4])
world.append(CP)

print(CP.contains(Punt(0,-0.5,1)))

p0x = -2
p0y = 3
p0z = 3
vd = Vector(Punt(1,0,0))
edges = [Punt(p0x,p0y,p0z)]
normal = []
for i in range(30):
    p0z = 3
    for j in range(30):
        vd = vd.norml()
        p0 = Punt(p0x,p0y,p0z)
        pf, coll, deg = vd.rycst(org=p0,length=5,world=world)
        edges.append(pf)
        if coll == "Plane":
            deg = np.sqrt(1-deg*deg)
            normal.append(deg)
        else:
            normal.append(0)
        #print(p0.get())
        p0z -= 0.2
    p0y -= 0.2

print(normal)
indexes = [len(charmap)-int(deg*len(charmap)) for deg in normal]
print(indexes)
result = [charmap[i] for i in indexes]
res = "".join(result)
for i in range(30):
    for j in range(30):
        print(res[30*i+j]*2,end="")
    print("")

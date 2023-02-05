import numpy as np
from graphics import *

TOL = 0.02
DIM = 500
SCL = 100
charmap = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

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
    def point_in_seg(self, p):
        ab = Vector(self.a,self.b)
        pa = Vector(p,self.a)
        pb = Vector(p,self.b)
        dnorm2 = pa.xprod(pb).norma()
        if dnorm2 < TOL:
            dnorm1 = np.abs(ab.norma()-(pa.norma()+pb.norma()))
            if dnorm1 < TOL*TOL:
                return True, ab
        return False, None

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
                col, seg = element.point_in_seg(endpoint)
                if col:
                    deg = self.degrr(seg)
                    # it should be deg*cc/length^2, but by the moment...
                    return endpoint, element, deg*cc/length #darker if further
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
#win = GraphWin('title', DIM, DIM)
world = []
for i in range(4):
    p1 = Punt(np.random.rand()*2-1,np.random.rand()*2-1,0)
    p2 = Punt(np.random.rand()*2-1,np.random.rand()*2-1,0)
    s = Segment(p1,p2,colors[i],3)
    world.append(s)
    #s.draw_segment().draw(win)

p0 = Punt(-1,1.5,0)
vd = Vector(Punt(0,-1,0))
edges = [p0]
normal = []
for i in range(40):
    vd = vd.norml()
    pf, coll, deg = vd.rycst(org=p0,length=4,world=world)
    edges.append(pf)
    normal.append(deg)
    #sn = Segment(edges[-1],edges[-2],'black',1)
    #sn.draw_segment().draw(win)
    p0.x += 0.05
#sn = Segment(edges[-1],p0,'black',1)
#sn.draw_segment().draw(win)
indexes = [68-int(deg*69) for deg in normal]
result = [charmap[i] for i in indexes]
print("".join(result))
# win.getMouse()

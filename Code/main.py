import numpy as np

TOL = 0.01

def vbtw2(p, q):
    v = [q[i]-p[i] for i in range(3)]
    return v

def norma(v):
    return np.sqrt(np.sum([vi*vi for vi in v]))

def norml(v):
    n = norma(v)
    v = [round(vi/n,5) for vi in v]
    return v

def xprod(v, u):
    w = [v[1]*u[2]-v[2]*u[1],v[2]*u[0]-v[0]*u[2],v[0]*u[1]-v[1]*u[0]]
    w = [round(wi,5) for wi in w]
    return w

def rycst(og, vd, mu):
    return np.add(og, [vdi*mu for vdi in vd])

#punts de la lina l1
p1 = [1, 1, 0]
p2 = [-0.5, -1, 0]

#raycast
og = [-1, 3, 0] #original point
vd = [1, -4, 0] #director vector

dx = 0.025 #diferencial
mc = 1.1 #max cast distance (suposant que vd estigui normalitzat!!)
cc = 0 #current cast distace
while cc < mc:
    pr = rycst(og, vd, cc) #punt ray(cc)
    e1 = vbtw2(p1, p2) #vector segment p1p2
    e2 = vbtw2(p1, pr) #vector entre p1 i raycast
    xp = xprod(e1, e2)
    if norma(xp)<TOL: print("HIT")
    print(norma(xp),pr)
    cc += dx

import numpy as np

def rotate(v, b):
    ux = v[0]*np.cos(b)-v[1]*np.sin(b)
    uy = v[1]*np.cos(b)+v[0]*np.sin(b)
    return [ux, uy, 0]

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

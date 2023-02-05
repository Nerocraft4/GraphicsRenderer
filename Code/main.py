from utils import *

TOL = 0.01

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

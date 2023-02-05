from graphics import *
import numpy as np

def rotate(v, b):
    ux = v[0]*cos(b)-v[1]*sin(b)
    uy = v[1]*cos(b)+v[0]*sin(b)
    return [ux, uy]

DIM = 500
def mkpoint(x, y):
    x = x + DIM/2
    y = DIM/2 - y
    return Point(x, y)

def main():
    win = GraphWin('title', DIM, DIM)
    pt = mkpoint(-60,-100)
    line = Line(pt, mkpoint(100, 60))
    line.setWidth(3)
    line.draw(win)
    og = mkpoint(-150, 150)
    ry = [0.5,-3]
    
    og.draw(win)

    win.getMouse()
main()

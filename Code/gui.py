from graphics import *

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

from AreaOfPolygon import getArea

def Left(a, b, c):
    return getArea([a, b, c]) > 0


def LeftOn(a, b, c):
    return getArea([a, b, c]) >= 0


def Collinear(a, b, c):
    return getArea([a, b, c]) == 0

def Between(a, b, c):
    if not Collinear(a, b, c):
        return False
    if a[0]!=b[0]:
        return ((a[0]<=c[0]) and (c[0]<=b[0])) or ((a[0]>=c[0]) and (c[0]>=b[0]))
    else:
        return ((a[1]<=c[1]) and (c[1]<=b[1])) or ((a[1]>=c[1]) and (c[1]>=b[1]))

def intersectProper(p1, q1, p2, q2):
    c1 = Collinear(p1, q1, p2)
    c2 = Collinear(p1, q1, q2)
    c3 = Collinear(p2, q2, p1)
    c4 = Collinear(p2, q2, q1)

    if c1 or c2 or c3 or c4:
        return False
    else:
        return Left(p1, q1, p2) == Left(p1, q1, q2) and Left(p2, q2, p1) == Left(p2, q2, q1)

def intersect(a, b, c, d):
    if intersectProper(a, b, c, d):
        return True
    elif (Between(a, b, c) or Between(a, b, d) or Between(c, d, a) or Between(c, d, b)):
        return True
    else:
        return False
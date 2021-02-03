from Intersection import Left, LeftOn, intersect

polygonArray=[]
n=0

def inCone(a, b):
    idx = polygonArray.index(a)
    a1 = polygonArray[(idx+1)%n]
    a0 = polygonArray[(idx-1)%n]

    if LeftOn(a, a1, a0):
        return Left(a, b, a0) and Left(b, a, a1)
    else:
        return not (LeftOn(a, b, a0) and LeftOn(b, a, a1))

def Diagonalie(a, b):
    for i in range(n):
        curPoint = polygonArray[i]
        nextPoint = polygonArray[(i+1)%n]
        if (curPoint!=a and nextPoint!=a) and (curPoint!=b and nextPoint!=b) and intersect(a, b, curPoint, nextPoint):
            return False
    return True

def isDiagonal(polygon, a, b):
    global polygonArray
    global n
    polygonArray = polygon[:]
    n = len(polygon)
    return(inCone(a,b) and inCone(b,a) and Diagonalie(a,b))
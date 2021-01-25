def inputPolygon(numberOfPoints):
    polygonArray = []
    print("Enter the points in cyclic order. Each point is represented by space-separated coordinates.")
    for i in range(numberOfPoints+1):
        x,y = map(int, input().split())
        polygonArray.append(tuple([x,y]))
        
    if isValidPolygon(numberOfPoints, polygonArray):
        return polygonArray
    else:
        return None

def printPolygon(polygonArray):
    for count,point in enumerate(polygonArray):
        print(count+1, "     ", point)

def isValidPolygon(numberOfPoints, polygonArray):
    if numberOfPoints<3 or polygonArray[0]!=polygonArray[numberOfPoints]:
        print("The 2D object is not a Polygon.")
        return False
    else:
        print("The 2D object is a Polygon.")
        return True

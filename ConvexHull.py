def turn(points, n):
    p1 = points[n-2]
    p2 = points[n-1]
    p3 = points[n]
    return (p2[0]- p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def convexUpper(polygonArray, numberOfPoints):
    solutionUpper = []
    solutionUpper.append(polygonArray[0])
    solutionUpper.append(polygonArray[1])
    numberOfPoints = 2
    
    for i in range(2, numberOfPoints):
        solutionUpper.append(polygonArray[ i])
        numberOfPoints += 1
        while numberOfPoints > 2 and turn(solutionUpper, numberOfPoints - 1) >= 0:
            solutionUpper.pop(numberOfPoints-2)
            numberOfPoints -= 1
    return solutionUpper

def convexLower(polygonArray, numberOfPoints):
    l = len(polygonArray) 
    solutionLower = []
    solutionLower.append(polygonArray[l - 1])
    solutionLower.append(polygonArray[l - 2])
    numberOfPoints = 2
    
    for i in range(l - 2, -1, -1):
        solutionLower.append(polygonArray[ i])
        numberOfPoints += 1
        while numberOfPoints > 2 and turn(solutionLower, numberOfPoints - 1) >= 0:
            solutionLower.pop(numberOfPoints-2)
            numberOfPoints -= 1
    return solutionLower

def convexHull(polygonArray, numberOfPoints):
    if numberOfPoints<3:
        return False
    else:
        polygonArray.sort(key=lambda x: (x[0], x[1]))
        
        solutionUpper = convexUpper(polygonArray, numberOfPoints)
        solutionLower = convexLower(polygonArray, numberOfPoints)
        
        solutionUpper.pop()
        solutionLower.pop()
        
        sol = solutionUpper + solutionLower
    
        return sol
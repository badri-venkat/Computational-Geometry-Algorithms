def getArea(polygonArray):
    numberOfPoints = len(polygonArray)
    areaOfPolygon = 0

    for i in range(numberOfPoints):
        areaOfPolygon += polygonArray[i][0] * polygonArray[(i + 1)%numberOfPoints][1]
        areaOfPolygon -= polygonArray[i][1] * polygonArray[(i + 1)%numberOfPoints][0]

    return areaOfPolygon/2.0

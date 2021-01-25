from PolygonHelper import inputPolygon

numberOfPoints = int(input("Number of Points? : "))
polygonArray = inputPolygon(numberOfPoints)

areaOfPolygon=0

for i in range(numberOfPoints):
    areaOfPolygon+=polygonArray[i][0] * polygonArray[i+1][1]
    areaOfPolygon-=polygonArray[i][1] * polygonArray[i+1][0]

print(areaOfPolygon)
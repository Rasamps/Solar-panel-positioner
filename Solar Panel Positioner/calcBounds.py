def calcBounds(coordArr):
    print('Select a distance to search away from your centered point, this will be measured in kilometres.')
    distance = input()
    boundsArr = []
    topLeft = [(coordArr[0] + (1/111)*(float(distance))),(coordArr[1] + (1/111)*(float(distance)))]
    topRight = [(coordArr[0] - (1/111)*(float(distance))),(coordArr[1] - (1/111)*(float(distance)))]
    boundsArr = [topLeft, topRight]
    ##print(boundsArr)
    return boundsArr

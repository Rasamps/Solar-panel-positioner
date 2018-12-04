def infoReturn(bestCoords, angles, direction):
    bestCoords = list(bestCoords)
    print("Our final report based on your location, and requests for angle system result in...\n")
    print("You should position your solar panels at:")
    print("\t--> ", bestCoords[0], bestCoords[1])
    print("\n")
    print("The solar panels, from the horizontal, should be angled at:")

    if(len(angles) == 1):
        print("\t--> ",angles[0], "pointed",direction)
    elif(len(angles) == 2):
        print("\t--> ",angles[0], "for the summer and,", angles[1], "for the winter pointed",direction)
    elif(len(angles) == 3):
        print("\t--> ",angles[0], "for the summer,", angles[1], "for the winter and,", angles[2], "for the spring and fall pointed",direction)

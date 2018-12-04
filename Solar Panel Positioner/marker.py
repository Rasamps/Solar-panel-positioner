import googlemaps
from googlemaps import convert
import numpy as np
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAftRNXU6CGaRywPKe_z-vvEhLspDwhgVE')

def optimalMarker(bounds):
    #bounds have structure [[TLlat,Tllong],[BRlat,BRlong]]
    #place markers
    markers = [[],[]]
    ##divide into a "box" bounds is just the edges broken into 10 intervals
    ##markers[0] is list of latitude, markers[1] is list of longitudes
    ##combination will give markers
    markers[0] = np.linspace(bounds[0][0],bounds[1][0],num=10) ##Latitudes
    markers[1] = np.linspace(bounds[0][1],bounds[1][1],num=10) ##Longitudes
    #pairs of marker coordinates
    pairs = [[0 for x in range(2)]for y in range(100)]
    count = 0
    for i in range(10):
        for j in range(10):
            pairs[count] = [markers[0][i], markers[1][j]]
            count += 1
    ##find max elevation of the markers

    maxElevation = 0
    maxMarker = pairs[0]
    for k in range(100):

        marker = (pairs[k][0], pairs[k][1])
        elevation = gmaps.elevation(marker)[0]['elevation']
        if elevation > maxElevation:
            maxElevation = elevation
            maxMarker = marker

    #print("Coords: " + str(maxMarker) + " Height: " + str(maxElevation))
    return maxMarker

##optimalMarker([[43.14456,72.44321],[42.91123,72.63234]])

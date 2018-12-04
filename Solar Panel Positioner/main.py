##Following lines import our functions from exterior python files and the google maps API.
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAftRNXU6CGaRywPKe_z-vvEhLspDwhgVE')
from calcBounds import calcBounds
from optAngles import *
from solarDirection import determineDir
from marker import optimalMarker
from format import infoReturn

##The main function makes all necessary calls to outside functions and runs the main log for the script.
def main():
    print('Welcome to the Solar Panel Positioner. To begin how would you like to select your central point to search around. Either type address or coordinates.')
    loop1 = True
    while(loop1 == True): ##While loop is because of user input, in case they don't enter the correct option
                           ##we can loop again
        locationType = input()

        if (locationType == 'address'): ##Depending on input we have to consider certain conditions
            print('You have selected address as your location type.')
            userAddress = input("Enter Address \n")
            geocode_results = gmaps.geocode(userAddress)
            geocode_results = [geocode_results[0]['geometry']['location']['lat'],geocode_results[0]['geometry']['location']['lng']]
            ##print(geocode_results)
            searchBounds = calcBounds(geocode_results)
            optimalSpot = optimalMarker(searchBounds)
            angles = optimalAngles(geocode_results[0])
            direction = determineDir(geocode_results[1])
            print(infoReturn(optimalSpot, angles, direction))
            loop1 = False

        elif (locationType == 'coordinates'):
            print('You have selected coordinates, please enter them.')
            geocode_results = input()
            geocode_results = geocode_results.split(',')
            geocode_results[0] = float(geocode_results[0])
            geocode_results[1] = float(geocode_results[1])
            ##print(geocode_results)
            searchBounds = calcBounds(geocode_results)
            optimalSpot = optimalMarker(searchBounds)
            angles = optimalAngles(geocode_results[0])
            direction = determineDir(geocode_results[1])
            print(infoReturn(optimalSpot, angles, direction))
            loop1 = False

        else:
            print('This is not a valid option please input either *address* or *coordinates*.')

main()

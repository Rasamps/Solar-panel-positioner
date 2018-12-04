import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAftRNXU6CGaRywPKe_z-vvEhLspDwhgVE')

def determineDir(longitude):
    if(longitude > 0):
        return 'South'
    else:
        return 'North'

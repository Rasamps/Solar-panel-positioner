import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAftRNXU6CGaRywPKe_z-vvEhLspDwhgVE')

def optimalAngles(lati):
    loop2 = True
    print('When using solar panels there are three options. They include a year-round fixed position, two-season, or four-season system.')
    print("Please type either: fixed, two-season or four-season")
    sysChoice = input('Which system would you like?\n')
    while(loop2 == True):
        if(sysChoice == "fixed"):
            optAng = fixedAng(lati)
            return optAng
        elif(sysChoice == "two-season"):
            optAng = twoSeas(lati)
            return optAng
        elif(sysChoice == "four-season"):
            optAng = fourSeas(lati)
            return optAng
        else:
            print("That was not a correct input please try again.")

def fixedAng(lati):
    print("When selecting a fixed angle for the entire year it is important to think about when you need the most power.")
    print("If it is winter type winter, if it is summer type summer, if it is either the spring or fall type sf, if it is none of the previous options type none. **Do not use capital letters**")
    seasonChoice = input("Choose a season.\n")
    loop3 = True
    while(loop3 == True):
        if(seasonChoice == "winter"):
            angle = (lati*0.9) + 29
            return [angle]
        elif(seasonChoice == "summer"):
            angle = (lati*0.9) - 23.5
            return [angle]
        elif(seasonChoice == "sf"):
            angle = lati-2.5
            return [angle]
        elif(seasonChoice == "none"):
            if (lati < 25):
                angle = lati*0.87
                return [angle]
            elif(25 <= lati <= 50):
                angle = (lati*0.76) + 3.1
                return [angle]
            else:
                angle = (((lati*0.9)+29) + ((lati*0.9)-23.5))/2
                return [angle]
        else:
            print("This was not a valid option, input a correct keyword")

def twoSeas(lati):
    summerAng = (lati*0.9)-23.5
    winterAng = (lati*0.9)+29
    return [summerAng, winterAng]

def fourSeas(lati):
    summerAng = (lati*0.9)-23.5
    winterAng = (lati*0.9)+29
    springFallAng = lati - 2.5
    return [summerAng, winterAng, springFallAng]

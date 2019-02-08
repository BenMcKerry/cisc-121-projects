#Author: Ben McKerry
#Title: Superhero Kittens
#Decscription: Generates superhero kitten name based on last digit of ASCII value of actual names

#This function calculates the total ASCII value of the input in function askForName
def calculateTotalASCIIValue(calc):
    global ASCIITotal
    ASCIITotal = 0
    for i in range (0, len(calc)): 
        ASCIITotal += ord(calc[i])
    return ASCIITotal

#Asks for your first name 
def askForFirstName():
    name = input("Enter your first name: ")
    print("")
    return name

#Asks for your last name 
def askForLastName():
    name = input("Enter your last name: ")
    print("")
    return name

#List of all superhero prefixes
listOfSuperheroPrefixes = ['Super', 'Ultra', 'Marvel', 'Mega',
                           'Laser','Lightning', 'Thunder',
                           'Power', 'Iron', 'Captain']

#List of all kitten suffixes
listOfKittenSuffixes = ['Fuzz', 'Whiskers', 'Purr', 'Paw',
                         'Claw', 'Fang', 'Snuggle', 'Cuddle',
                         'Cute Overload', 'Socks']


#Main Function
def main():
    calculateTotalASCIIValue(askForFirstName())
    firstNameASCII = ASCIITotal%10 #Finding last digit of ASCII value
    prefix = listOfSuperheroPrefixes[firstNameASCII] #Using the above digit to find Superhero Prefix
    calculateTotalASCIIValue(askForLastName())
    lastNameASCII = ASCIITotal%10 #Finding last digit of ASCII value
    suffix = listOfKittenSuffixes[firstNameASCII] #Using the above digit to find Superhero Suffix
    return ("Your Superhero Kitten name is %s %s"%(prefix, suffix))
    
#Author: Ben McKerry
#Title: Space Junk
#Decscription: Finds all the space junk in a .bdi file

#Reads .bdi file, puts info into 2D list
def readBasicDigitalImageFile():
    spaceList2D = []
    spaceList = open("space.bdi").readlines()#putting file lines into 1D list
    for i in range(len(spaceList)):
        spaceList2D.append(spaceList[i].split())#lines from 1D list into individual chars in 2D list
    return spaceList2D

#Checks 2D list for any 1s surrounded by 0s
def isPixelSpaceJunk(spaceList2D):
    count = 0 #count of total space junk found
    for i in range(1,len(spaceList2D)):
        for j in range(1,len(spaceList2D)):
            if spaceList2D[i][j] == "1": #checking if the current pixel is a 1
                if spaceList2D[i-1][j-1] == "0" and \
                   spaceList2D[i-1][j] == "0" and \
                   spaceList2D[i-1][j+1] == "0" and \
                   spaceList2D[i][j-1] == "0" and \
                   spaceList2D[i][j+1] == "0" and \
                   spaceList2D[i+1][j-1] == "0" and \
                   spaceList2D[i+1][j] == "0" and \
                   spaceList2D[i+1][j+1] == "0":
                    spaceJunk = True
                else:
                    spaceJunk = False
                if spaceJunk == True:
                    print ("Space junk at %d, %d" % (i, j)) #printing co-ordinates of found space junk
                    count += 1 #increasing space junk total
    return ("There are %d instances of space junk." % (count))

#Main funtion using the other 2 functions above
def main2(): 
   return isPixelSpaceJunk(readBasicDigitalImageFile())
    
                   
            
            


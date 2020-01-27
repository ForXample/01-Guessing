import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

import random
nMin = 1
nMax = 100
nGuess = None
nResult = None
nCount = 0
nDistance = 0
nPreDistance = nMax - nMin
nResult = random.randint(nMin, nMax)

#print(nResult)
#store the player's guess into the nGuess
nGuess = input("Hohoho, welcome to the guessing game! Guess a number between %d and %d, and remember - you have unlimited time with unlimited chances~:\n" %(nMin,nMax))
while(True):
    if not nGuess.isdigit():
        nGuess = input("This is not funny~ Play by the rules, shall we? Please try again.\n")
    elif int(nGuess) < nMin or int(nGuess) > nMax:
        nGuess = input("Rules are rules, you have to guess a number that is between 1 to 100. Please try again.\n")
    else:   #the player's guess should be legit this time
        nCount += 1
        if nResult == int(nGuess):  #bingo
            break
        else:
            nDistance = abs(nResult - int(nGuess)) 
            if nDistance <= nPreDistance:   #if the nPredistance is getting longer than the nDistance
                nPreDistance = nDistance    #if the distance is shorter, give the value of nPreDistance to nDistance
                nGuess = input("Awww, you are getting close！C'mon, try again!\n") #closer
            else:
                nGuess = input("Whoa whoa whoa, you are getting way ahead. Try again!\n") #farther

print("Amazing! I knew you can do it! See ya~ \n \nReport: The correct answer is %d. Total attempts = %d"%(nResult, nCount))
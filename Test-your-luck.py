import random

levels = 10
currentLevel = 1

enemyNames = [
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
    "sdofjsdf",
]

# This function shows the game instructions 
def displayInstructions():
    gameInstructions = "There are 10 levels. Player has to choose 1 or 2. If it's correct you move on to the next level."


userResponse = input( "\n<<<<<< Hit enter to start: Press ENTER: >>>>>>" )


userResponse = input( "Do you want a tutorial Y/N: " )



while currentLevel <= levels:
    if userResponse.lower() == "y":
        displayInstructions()

    currentLevel = currentLevel + 1

    print("Good luck!!!")
    computerRandomNumber = random.randint(1,2)
    #print( computerRandomNumber ) # Cheating

    userNumber = int(input( f"Monster {enemyNames[ currentLevel ]}>>>>>>>> What's your number?: " ) )

    while userNumber not in [1, 2]:
        print( "Don't be silly, type in 1 or 2" )

    if computerRandomNumber == userNumber:
        print( f"You're lucky, my buddy will get you in level {currentLevel}" )
    else:
        break

if currentLevel >= 10:
    print( "You won!!!!" )
else:
    print( "Hahaha, we got you" )
# if level == 10:
#     print ("you survived the night")
# elif level < 10:
#     input("1 or 2? ")
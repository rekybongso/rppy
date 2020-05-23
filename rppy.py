from modules import engine
from modules.utils import clearScreen, makeScreen, getValidInput, randomizeBotOutput, changeTextColor

play = True

playerScore = [0]
botScore = [0]
roundPlayed = [0]

phrasesToAccept = ("y", "yes", "g", "go", "yeah", "sure")
phrasesToDecline = ("n", "no", "stop", "nope", "bye")

while (play):    
    clearScreen()
    makeScreen()

    playerInput = getValidInput("Your pick > ")
    botInput = randomizeBotOutput()

    gameMechanic = engine.GameMechanics(playerInput, botInput, playerScore, 
                                    botScore, roundPlayed)
                                            
    gameMechanic.playGame()
    repeat = True

    while (repeat):
        askToRepeat = input("Play again (y: yes | n: no)? ").lower()

        if askToRepeat in phrasesToAccept:
            break
        elif askToRepeat in phrasesToDecline:
            play = False
            break
        else:
            print(changeTextColor("Unkown choice received. Please try again!", "yellow"))
            
from modules import game_engine, utils

gameUtility = utils.MainFunctions()

play = True

playerScore = [0]
botScore = [0]
roundPlayed = [0]

while (play):    
    gameUtility.clearScreen()
    gameUtility.makeScreen()

    playerInput = gameUtility.getValidInput("Your pick > ")
    botInput = gameUtility.randomizeBotOutput()

    gameMechanic = game_engine.Mechanics(playerInput, botInput, playerScore, 
                                            botScore, roundPlayed)
                                            
    gameMechanic.playGame()
    repeat = True

    while (repeat):
        askToRepeat = input("Play again (y: yes | n: no)? ").lower()

        if askToRepeat in ("y", "yes"):
            break
        elif askToRepeat in ("n", "no"):
            play = False
            break
        else:
            print ("Unkown choice received. Please try again!")
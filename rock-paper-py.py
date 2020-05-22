from modules import game_engine

gm = game_engine.MainMechanic()

play = True

while (play):    
    gm.clearTheScreen()
    gm.makeScreen()

    playerInput = gm.getValidInput("Your pick > ")
    botInput = gm.randomizeBotOutput()

    gm.playTheGame(playerInput, botInput)

    while (True):
        askToRepeat = input("Play again (y: yes | n: no)? ").lower()

        if askToRepeat in ("y", "yes"):
            break
        elif askToRepeat in ("n", "no"):
            play = False
            break
        else:
            print ("Unkown choice received. Please try again!")
    
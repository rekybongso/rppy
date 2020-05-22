import random
from os import system, name

class MainMechanic:

    def clearTheScreen(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    
    def makeScreen(self):
        print('''
        ----------------------------
        - Welcome to rock-paper-py -
        ----------------------------

        Instruction:
        1) Please type between rock, paper, or scissor
        2) You can also input the first char from each available choices eg: r for rock
        3) Have fun! 
        ''')

    def getValidInput(self, prompMessageToUser):
        acceptedInput = ("rock","paper","scissor", "r", "p", "s")
        repeatCheckInput = True

        while (repeatCheckInput):

            userInputToCheck = input(prompMessageToUser).lower()

            if (userInputToCheck.isspace()) or \
                (userInputToCheck.isalpha() == False) or \
                (userInputToCheck not in acceptedInput):

                print ("Invalid input received. Please try again!")

            else:
                userInputToCheck = self.doTransfromInput(userInputToCheck)

                validOutput = userInputToCheck
                repeatCheckInput = False
                
        return validOutput
        
    def doTransfromInput(self, inputToTransform):
        originInput = inputToTransform

        switchOutput = {
            "r": "rock",
            "p": "paper",
            "s": "scissor"
        }

        finalOutput = switchOutput.get(originInput, "nothing")

        if finalOutput == "nothing":
            return originInput
        else:
            return finalOutput

    def randomizeBotOutput(self):
        botChoices = ("rock", "paper", "scissor")
        botOutput = random.choice(botChoices)
        return botOutput
    
    def isGameTie(self, playerInput, botInput):
        return playerInput == botInput
    
    def isPlayerWin(self, playerInput, botInput):
        return (playerInput == "scissor" and  botInput == "paper") or \
            (playerInput == "rock" and botInput == "scissor") or \
            (playerInput == "paper" and botInput == "rock")

    def decideTheResult(self, playerInput, botInput):
        player = playerInput
        bot = botInput

        if self.isGameTie(player, bot) == True:
            return "Game is tie!"
        else:
            if self.isPlayerWin(player, bot) == True:
                return "Player win"
            else:
                return "Player lose"

    def playTheGame(self, playerInput, botInput):
        player = playerInput
        bot = botInput

        gameResult = self.decideTheResult(player, bot)
            
        print (
            " Player pick", player, "\n",
            "Bot pick", bot, "\n",
            gameResult
        )

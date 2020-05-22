import random
from os import system, name

class MainFunctions:
    
    def clearScreen(self):
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

    def randomizeBotOutput(self):
        botChoices = ("rock", "paper", "scissor")
        botOutput = random.choice(botChoices)

        return botOutput

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
                userInputToCheck = self.transfromInput(userInputToCheck)

                validOutput = userInputToCheck
                repeatCheckInput = False
                
        return validOutput
        
    def transfromInput(self, inputToTransform):
        originalOutput = inputToTransform

        transformOutput = {
            "r": "rock",
            "p": "paper",
            "s": "scissor"
        }

        finalOutput = transformOutput.get(originalOutput, "nothing")

        if finalOutput == "nothing":
            return originalOutput
        else:
            return finalOutput
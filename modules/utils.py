import random
from os import system, name

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
def makeScreen():
    print('''
    ----------------------------
    - Welcome to rock-paper-py -
    ----------------------------

    Instruction:
    1) Please type between rock, paper, or scissor
    2) You can also input the first char from each available choices eg: r for rock
    3) Have fun! 
    ''')

def randomizeBotOutput():
    botChoices = ("rock", "paper", "scissor")
    botOutput = random.choice(botChoices)

    return botOutput

def getValidInput(prompMessageToUser):
    acceptedInput = ("rock","paper","scissor", "r", "p", "s")
    repeatCheckInput = True

    while (repeatCheckInput):

        userInputToCheck = input(prompMessageToUser).lower()

        if (userInputToCheck.isspace()) or \
            (userInputToCheck.isalpha() == False) or \
            (userInputToCheck not in acceptedInput):

            print(changeTextColor("Invalid input received. Please try again!", "yellow"))

        else:
            userInputToCheck = transfromInput(userInputToCheck)

            validOutput = userInputToCheck
            repeatCheckInput = False
                
    return validOutput
        
def transfromInput(inputToTransform):
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

def changeTextColor(textInput, color):
    colorPlates = {
        "red": '\33[31m',
        "green": '\33[32m',
        "yellow": '\33[33m',
        "blue": '\33[34m',
        "cyan": '\33[36m'
    }

    colorReset = '\33[m'
    selectedColor = colorPlates.get(color.lower(), colorReset)

    return (selectedColor + str(textInput) + colorReset)
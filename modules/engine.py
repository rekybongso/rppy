from modules.utils import changeTextColor

class GameMechanics:

    def __init__(self, playerInput, botInput, playerScoreList, botScoreList, roundPlayed):
        self.roundPlayed = roundPlayed
        self.playerInput = playerInput
        self.playerScoreList = playerScoreList
        self.botInput = botInput
        self.botScoreList = botScoreList
        
    def getRoundsPlayed(self):
        roundList = self.roundPlayed

        prevRound = roundList[-1]
        nextRound = prevRound + 1

        roundList.append(nextRound)
        currentRound = int(roundList[-1])

        return currentRound

    def getPlayerScore(self):
        scoreList = self.playerScoreList
        scoreResult = int(scoreList[-1])

        return scoreResult

    def getBotScore(self):
        scoreList = self.botScoreList
        scoreResult = int(scoreList[-1])

        return scoreResult

    def addPlayerScore(self):
        lastScore = self.getPlayerScore()
        newScore = lastScore + 1

        scoreList = self.playerScoreList
        scoreList.append(newScore)

        scoreResult = self.getPlayerScore()

        return scoreResult
    
    def addBotScore(self):
        lastScore = self.getBotScore()
        newScore = lastScore + 1

        scoreList = self.botScoreList
        scoreList.append(newScore)

        scoreResult = self.getBotScore()
        
        return scoreResult

    def varAdapter(self):
        roundPlayed = changeTextColor(self.getRoundsPlayed(), "cyan")
        playerInput = changeTextColor(self.playerInput.upper(), "blue")
        botInput = changeTextColor(self.botInput.upper(), "red")

        return roundPlayed, playerInput, botInput    

    def isGameTie(self):
        return self.playerInput == self.botInput
    
    def isPlayerWin(self):
        playerInput = self.playerInput
        botInput = self.botInput

        return (playerInput == "scissor" and  botInput == "paper") or \
            (playerInput == "rock" and botInput == "scissor") or \
            (playerInput == "paper" and botInput == "rock")

    def gameResult(self):
        if self.isGameTie() == True:
            return "tie"
        elif self.isPlayerWin() == True:
            return "win"
        else:
            return "lose"

    def playGame(self):
        getResult = self.gameResult()
        showResult = getattr(self, getResult, lambda: "None")

        return showResult()

    def tie(self):
        playerScore = changeTextColor(self.getPlayerScore(), "green")
        botScore = changeTextColor(self.getBotScore(), "green")

        adaptRoundPlayed, adaptPlayerInput, adaptBotInput = self.varAdapter()

        print("\nRounds:", adaptRoundPlayed)
        print(
            "\n Player pick", adaptPlayerInput, "\n",
            "Bot pick", adaptBotInput, "\n"
            " \nNo winner! Game is a Tie!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)
    
    def win(self):
        playerScore = changeTextColor (self.addPlayerScore(), "green")
        botScore = changeTextColor (self.getBotScore(), "green")

        adaptRoundPlayed, adaptPlayerInput, adaptBotInput = self.varAdapter()

        print("\nRounds:", adaptRoundPlayed)
        print(
            "\n Player pick", adaptPlayerInput, "\n",
            "Bot pick", adaptBotInput, "\n"
            " \nPlayer win!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)
    
    def lose(self):
        playerScore = changeTextColor (self.getPlayerScore(), "green")
        botScore = changeTextColor (self.addBotScore(), "green")  

        adaptRoundPlayed, adaptPlayerInput, adaptBotInput = self.varAdapter()

        print("\nRounds:", adaptRoundPlayed)
        print(
            "\n Player pick", adaptPlayerInput, "\n",
            "Bot pick", adaptBotInput, "\n"
            " \nBot win!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)

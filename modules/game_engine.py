class Mechanics:

    def __init__(self, playerInput, botInput, playerScoreList, botScoreList, roundPlayed):
        self.roundPlayed = roundPlayed
        self.playerInput = playerInput
        self.playerScoreList = playerScoreList
        self.botInput = botInput
        self.botScoreList = botScoreList

    def countRound(self):
        roundList = self.roundPlayed

        prevRound = roundList[-1]
        nextRound = prevRound + 1
        roundList.append(nextRound)

        thisRound = int(roundList[-1])

        return thisRound

    def addPlayerScore(self):
        scoreList = self.playerScoreList

        lastScore = scoreList[-1]
        newScore = lastScore + 1
        scoreList.append(newScore)

        scoreResult = self.getPlayerScore()

        return scoreResult
    
    def getPlayerScore(self):
        scoreList = self.playerScoreList
        scoreResult = int(scoreList[-1])

        return scoreResult

    def addBotScore(self):
        scoreList = self.botScoreList

        lastScore = scoreList[-1]
        newScore = lastScore + 1
        scoreList.append(newScore)

        scoreResult = self.getBotScore()
        
        return scoreResult

    def getBotScore(self):
        scoreList = self.botScoreList
        scoreResult = int(scoreList[-1])

        return scoreResult

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
        playerScore = self.getPlayerScore()
        botScore = self.getBotScore()
        roundPlayed = self.countRound()

        print("\nRounds:", roundPlayed)
        print(
            "\n Player pick", self.playerInput.upper(), "\n",
            "Bot pick", self.botInput.upper(), "\n"
            " \nNo winner! Game is a Tie!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)
    
    def win(self):
        playerScore = self.addPlayerScore()
        botScore = self.getBotScore()
        roundPlayed = self.countRound()

        print("\nRounds:", roundPlayed)
        print(
            "\n Player pick", self.playerInput.upper(), "\n",
            "Bot pick", self.botInput.upper(), "\n"
            " \nPlayer win!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)
    
    def lose(self):
        playerScore = self.getPlayerScore()
        botScore = self.addBotScore()
        roundPlayed = self.countRound()

        print("\nRounds:", roundPlayed)
        print(
            "\n Player pick", self.playerInput.upper(), "\n",
            "Bot pick", self.botInput.upper(), "\n"
            " \nBot win!\n"
            )

        print("Player score:", playerScore, " | ", "Bot Score:", botScore)
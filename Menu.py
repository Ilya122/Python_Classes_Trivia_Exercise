from PlayerNameGenerator import PlayerNameGenerator
from Game import Game
from QuestionsLoader import JsonTriviaQuestionsloader
from ActivePlayers import ActivePlayers


class Menu:
    def __init__(self):
        self.__activePlayers = ActivePlayers()
        self.__questionsGenerator = JsonTriviaQuestionsloader()
        self.__pointsToWin = 10

    def Execute(self):
        wantsToPlay = True
        hasPlayed = False
        while wantsToPlay:

            userInput = input('Please Enter to Begin, C to exit: ')
            if userInput == 'c' or userInput == 'C':
                break

            categories = self.__questionsGenerator.Load()

            game = Game(self.__activePlayers, categories, self.__pointsToWin)
            game.Run()
            hasPlayed = True

        if hasPlayed:
            print('Thanks for playing!')
        else:
            print('Hope you\'ll play next time!')

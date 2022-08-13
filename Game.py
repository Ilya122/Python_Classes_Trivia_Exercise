from Utils import GetIntegerFromUser
import random
from ActivePlayers import ActivePlayers
from Models.Category import Category
from Models.Question import Question


class Game:
    def __init__(self, activePlayers: ActivePlayers, categories, pointsToWin):
        self.__players = activePlayers
        self.__categories = categories
        self.__pointsToWin = pointsToWin

    def Run(self):
        minPlayers = 2
        maxPlayers = 8
        numOfPlayers = GetIntegerFromUser(
            'Number of players: ', minPlayers, maxPlayers)
        self.__players.ResetPlayers(numOfPlayers)
        self.__printSeperateLine()
        playersInfo = self.__players.ToString()
        print(playersInfo, end='')
        self.__printSeperateLine()

        winner = ''

        while self.__areMoreQuestions() or self.__anyPlayerReachedGoal():
            playingPlayer = self.__players.GetNextPlayer()
            print(f'{playingPlayer.Name}\'s Turn!')
            self.__printSeperateLine()

            selectedCategory = self.__selectCategory()
            if selectedCategory is None:
                print('No more questions available!')
                break

            randQuestion = self.__getRandomQuestion(selectedCategory)
            self.__printSeperateLine()

            self.__answerQuestion(
                playingPlayer, randQuestion, selectedCategory)

            self.__printSeperateLine()

        winner = self.__getWinner()
        print(f'Winner is: {winner.Name} with {winner.Points} Points!')

    def __selectCategory(self):
        categoryNum = 1
        for category in self.__categories:
            if len(category.Questions) == category.AnsweredQuestions:
                continue
            print(f'{categoryNum}){category.Name}')
            categoryNum += 1

        if categoryNum == 1:
            return None

        # TODO: int parse + Bound check
        selected = GetIntegerFromUser('Select Category: ', 1, categoryNum)
        selectedCat = self.__categories[selected - 1]
        return selectedCat

    def __areMoreQuestions(self):
        for category in self.__categories:
            if len(category.Questions) != category.AnsweredQuestions:
                return True
        return False

    def __getRandomQuestion(self, selectedCategory: Category):
        amountOfQuestions = len(selectedCategory.Questions)
        selecting = True
        question: Question = ()

        while selecting:
            randomIndex = random.randint(0, amountOfQuestions - 1)
            question = selectedCategory.Questions[randomIndex]
            selecting = question.WasAnswered
        return question

    def __answerQuestion(self, player, question, category):
        pts = question.GetPoints()

        print(f'{question.Difficulty} question for {pts} points:')
        self.__printSeperateLine()
        print(question.ToString(), end='')

        questionAnswer = GetIntegerFromUser(
            "Select answer: ", 1, len(question.Answers))

        if questionAnswer - 1 == question.CorrectAnswerIndex:
            player.Points += pts
            category.AnsweredQuestions += 1
            question.WasAnswered = True
            print(f'Correct {player.Name} gets {pts} Points!')
        else:
            print('Incorrect!')

    def __printSeperateLine(self):
        print('============')

    def __anyPlayerReachedGoal(self):
        for player in self.__players.GetPlayers():
            if player.Points >= self.__pointsToWin:
                return True
        return False

    def __getWinner(self):
        playerWithMaxPoints = ''
        maxPoints = 0
        for player in self.__players.GetPlayers():
            if player.Points >= self.__pointsToWin:
                return player
            elif player.Points > maxPoints:
                playerWithMaxPoints = player
                maxPoints = player.Points
        return playerWithMaxPoints

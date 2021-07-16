import random
from PlayerNameGenerator import PlayerNameGenerator, BrooklynNameGenerator
from Models.Player import Player


class ActivePlayers:
    def __init__(self):
        self.__playerNameGenerator = BrooklynNameGenerator()
        self.__players = []
        self.__currentPlayerIndex = 0

    def GetNextPlayer(self):
        return self.__GetNextPlayer()

    def ResetPlayers(self, numOfPlayers):
        self.__currentPlayerIndex = 0
        self.__GeneratePlayers(numOfPlayers)

    def ToString(self):
        stringifed: str = ''
        stringifed += 'Players:\n'
        for index, player in enumerate(self.__players):
            stringifed += f'{index+1}){player.Name}\n'
        return stringifed

    def GetPlayers(self):
        return self.__players

    def __GeneratePlayers(self, numOfPlayers):
        self.__players = []
        for i in range(numOfPlayers):
            name = self.__playerNameGenerator.Generate()
            self.__players.append(Player(name))
        self.__RearrangePlayers()

    def __RearrangePlayers(self):
        random.shuffle(self.__players)

    def __GetNextPlayer(self):
        currentPlaying = self.__currentPlayerIndex
        self.__currentPlayerIndex = self.__currentPlayerIndex + 1
        if self.__currentPlayerIndex > len(self.__players) - 1:
            self.__currentPlayerIndex = 0
        return self.__players[currentPlaying]

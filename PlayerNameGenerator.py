import random

# Basic name generator interface
class PlayerNameGenerator:
    def Generate(self):
        pass

# Generating Brooklyn character names
class BrooklynNameGenerator(PlayerNameGenerator):
    def __init__(self):
        self.__usedIndices = []
        self.__names = ['Jake', 'Amy', 'Boyle',
                        'Terry', 'Roza', 'Gina',
                        'Holt', 'Scully', 'Hitchcock']

    def Generate(self):
        if len(self.__usedIndices) == len(self.__names):
            return ''

        length = len(self.__names)-1
        index = random.randint(0, length)
        while index in self.__usedIndices:
            index = random.randint(0, length)

        name = self.__names[index]
        self.__usedIndices.append(index)
        return name

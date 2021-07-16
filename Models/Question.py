class Question:
    def __init__(self, content, answers, correctAnswerIndex, difficulty, uniqueId):
        self.Content = content
        self.Answers = answers
        self.CorrectAnswerIndex = correctAnswerIndex
        self.Difficulty = difficulty
        self.UniqueId = uniqueId
        self.WasAnswered = False
        self.__difficulties = {'Easy': 1, 'Medium': 2, 'Hard': 3}

    def GetPoints(self):
        return self.__difficulties[self.Difficulty]

    def ToString(self):
        stringifed: str = ''
        stringifed = f'{self.Content}\n'
        index = 1
        for answer in self.Answers:
            stringifed += f'{index}){answer}\n'
            index += 1

        return stringifed

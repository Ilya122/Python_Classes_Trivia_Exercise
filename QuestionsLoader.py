import json
from Models.Category import Category
from Models.Question import Question
import random

# Loads through source questions
class TriviaQuestionsLoader:
    def Load(self):
        pass

# Loads the questions from a json file
class JsonTriviaQuestionsloader(TriviaQuestionsLoader):
    def __init__(self):
        self.FileName = 'Questions.json'
        pass

    def Load(self):
        categories = []
        with open(self.FileName, 'r') as file:
            categories = json.loads(file.read())

        retCategories = []
        cats = categories['Categories']

        for category in cats:
            catName = category['Name']
            catQuestions = category['Questions']
            createdQuestions = []
            for question in catQuestions:
                content = question['Content']
                answers = question['Answers']
                correct = question['CorrentAnswerIndex']
                diff = question['Difficulty']
                uniqueId = random.randint(0, 99999)
                createdQuestion = Question(
                    content, answers, correct, diff, uniqueId)
                createdQuestions.append(createdQuestion)

            createdCategory = Category(createdQuestions, catName)
            retCategories.append(createdCategory)

        return retCategories

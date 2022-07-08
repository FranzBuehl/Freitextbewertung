import json
import re

from entities.QuizSolution import QuizSolution
from helper.QuestionMapper import QuestionMapper

#
# def __init__(self):
#     # load Keywords
#     keywordFile = open("../assets/keywords.json", encoding="utf-8")
#     keywords = json.load(keywordFile)

def get_keywords(quizSolution: QuizSolution):
    keywordFile = open("keywordDetection/assets/keywords.json", encoding="utf-8")
    keywords = json.load(keywordFile)
    questionId = quizSolution.questionId
    solution = quizSolution.text
    pattern = keywords[QuestionMapper.get_name(questionId)]
    spans = []

    for match in re.finditer(pattern, solution):
        start, end = match.span()
        span = solution[start:end]
        if not span in spans:
            spans.append(span)

    return spans


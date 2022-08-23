import json
import re

from entities.Exercise import Exercise

def get_keywords(exercise: Exercise):
    keywordFile = open("keywordDetection/assets/keywords.json", encoding="utf-8")
    keywords = json.load(keywordFile)
    questionId = exercise.questionId
    solution = exercise.solution
    pattern = keywords[questionId]
    spans = []

    for match in re.finditer(pattern, solution):
        start, end = match.span()
        span = solution[start:end]
        if not span in spans:
            spans.append(span)

    return spans


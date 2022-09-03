import json
import os
import re

from entities.Exercise import Exercise

def get_keywords_in_exercise(exercise: Exercise):
    return get_keywords(exercise.questionId, exercise.solution)

def get_keywords(questionId: str, solution: str):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../assets/keywords.json')
    keywordFile = open(filename, encoding="utf-8")
    keywords = json.load(keywordFile)
    pattern = keywords[questionId]
    spans = []
    spansLower = []

    for match in re.finditer(pattern, solution):
        start, end = match.span()
        span = solution[start:end]
        if not span.lower() in spansLower:
            spansLower.append(span.lower())
            spans.append(span)

    return spans


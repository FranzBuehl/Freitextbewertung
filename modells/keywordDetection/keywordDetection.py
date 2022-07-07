import json
import re

from helper.QuestionMapper import QuestionMapper

# load Keywords
keywordFile = open("./assets/keywords.json", encoding="utf-8")
keywords = json.load(keywordFile)

questionId = 5
text = "störung wegen unterbrechungen"
pattern = keywords[QuestionMapper.getName(questionId)]

spans = []
for match in re.finditer(pattern, text):
    start, end = match.span()
    span = text[start:end]
    if not span in spans:
        spans.append(span)

print(spans, len(spans))

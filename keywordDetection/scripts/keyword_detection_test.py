import json

from keywordDetection.scripts.keyword_detection import get_keywords

testFile = open("../assets/test.json", encoding="utf-8")
testDatas = json.load(testFile)

initKeyValues = {"Arbeitsanalyse/Rollenunklarheit": 0,"Arbeitsanalyse/Informationsprobleme": 0,
                 "Arbeitsanalyse/Variabilität": 0, "Arbeitsanalyse/Tätigkeitsspielraum": 0,
                "Arbeitsanalyse/Zeitdruck": 0, "Arbeitsanalyse/Arbeitsunterbrechungen": 0,
                 "Arbeitsanalyse/Soziale Stressoren": 0, "Arbeitsanalyse/Feedback/Anerkennung": 0,
                 "Arbeitsanalyse/Soziale Unterstützung": 0, "Arbeitsgestaltung/Rollenunklarheit": 0,
                 "Arbeitsgestaltung/Informationsprobleme": 0, "Arbeitsgestaltung/Variabilität": 0,
                 "Arbeitsgestaltung/Tätigkeitsspielraum": 0, "Arbeitsgestaltung/Zeitdruck": 0,
                 "Arbeitsgestaltung/Arbeitsunterbrechungen": 0, "Arbeitsgestaltung/Soziale Stressoren": 0,
                 "Arbeitsgestaltung/Feedback/Anerkennung": 0, "Arbeitsgestaltung/Soziale Unterstützung": 0}
totalFound = initKeyValues.copy()
totalExpected = initKeyValues.copy()
correctFound = initKeyValues.copy()
errorCount = initKeyValues.copy()

for testData in testDatas:

    foundKeywords = get_keywords(testData["questionId"], testData["text"])
    totalFound[testData["questionId"]] += len(foundKeywords)

    expectedKeywords = testData["keywords"].copy()
    totalExpected[testData["questionId"]] += len(expectedKeywords)

    for keyword in foundKeywords:
        if keyword in expectedKeywords:
            expectedKeywords.remove(keyword)
            correctFound[testData["questionId"]] +=1

    #Are all Keywords found as expected?
    if len(expectedKeywords) > 0 or not len(foundKeywords) == len(testData["keywords"]):
        print(testData["questionId"], testData["text"])
        print("Warning: foundKeywords ", foundKeywords, " don't match the expectedKeywords ", testData["keywords"])
        errorCount[testData["questionId"]] += 1

for key in totalFound:
    questionPrecision = correctFound[key]/totalFound[key]
    questionRecall = correctFound[key]/totalExpected[key]
    print("For "+ key +":")
    print("precision : ", questionPrecision, "recall:", questionRecall, "F1:", (questionPrecision + questionRecall)/2)

precision = sum(correctFound.values())/sum(totalFound.values())
recall = sum(correctFound.values())/sum(totalExpected.values())

print("Total Values:")
print("precision : ", precision, "recall:", recall, "F1:", (precision + recall)/2)


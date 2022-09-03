import json

from semanticSimilarity.scripts.semantic_similarity import get_similarity_score

testFile = open("../assets/test.json", encoding="utf-8")
testPackages = json.load(testFile)

correctPrectictions = 0
falsePredictions = 0

for testPackage in testPackages:
    reference = testPackage[0]
    referenceValue = get_similarity_score(reference["questionId"], reference["solution"])

    packageCorrect = 0
    packageFalse = 0

    for exercise in testPackage:
        predictedValue = get_similarity_score(exercise["questionId"], exercise["solution"])

        if (predictedValue == referenceValue and exercise["similarityValue"] == "reference") or \
           (predictedValue > referenceValue and exercise["similarityValue"] == "higher") or \
           (predictedValue < referenceValue and exercise["similarityValue"] == "lower"):
            packageCorrect +=1
        else:    
            packageFalse += 1
            print("wrong predicted value:")
            print("reference:", referenceValue, reference["questionId"], reference["solution"])
            print("exercise:", predictedValue,  exercise["questionId"], exercise["solution"])

    correctPrectictions += packageCorrect
    falsePredictions += packageFalse

    print(reference["questionId"], "- precision:", packageCorrect/(packageCorrect+packageFalse))

print("Total precision:", correctPrectictions/(correctPrectictions+falsePredictions))

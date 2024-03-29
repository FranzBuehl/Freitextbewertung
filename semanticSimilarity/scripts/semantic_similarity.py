import os

import spacy_sentence_bert
import json

# load one of the models listed at https://github.com/MartinoMensio/spacy-sentence-bert/
nlp = spacy_sentence_bert.load_model('xx_stsb_xlm_r_multilingual')

#open file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../assets/sample_solutions.json')
file = open(filename, encoding='utf-8')

# returns JSON object as dictionary
sampleSolutions = json.load(file)


def get_similarity_score(questionId: str, playerSolution: str):
    sampleSolution = sampleSolutions[questionId]

    #make sure playerSolution ends with punctuation
    lastChar = playerSolution[len(playerSolution)-1]
    if not lastChar in ".?!":
        playerSolution += "."

    docSample = nlp(sampleSolution)
    docPlayer = nlp(playerSolution)

    return docSample.similarity(docPlayer)

file.close()

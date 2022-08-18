import spacy_sentence_bert
import json
from helper.QuestionMapper import QuestionMapper

# load one of the models listed at https://github.com/MartinoMensio/spacy-sentence-bert/
nlp = spacy_sentence_bert.load_model('xx_stsb_xlm_r_multilingual')

# Opening JSON file
file = open('semanticSimilarity/assets/sample_solutions.json', encoding='utf-8')
# returns JSON object as dictionary
sampleSolutions = json.load(file)


def get_similarity_score(questionId: int, playerSolution: str):
    sampleSolution = sampleSolutions[QuestionMapper.get_name(questionId)]
    doc1 = nlp(sampleSolution)
    doc2 = nlp(playerSolution)
    return doc1.similarity(doc2)

file.close()

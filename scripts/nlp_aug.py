import json
import timeit

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas


def set_category(category: str):
    output = {}
    for cat in sampleSolutions.keys():
        competenceLen = len('Arbeitsgestaltung/')
        catName = cat[competenceLen:]
        if cat == category:
            output[catName] = 1.0
        else:
            output[catName] = 0.0
    return output

def add_to_output(texts: [str], category: str):
    for text in texts:
        line = {'text': text, 'cats': set_category(category)}
        output.append(line)

# Opening JSON file
file = open('../semanticSimilarity/assets/sample_solutions.json', encoding='utf-8')
# returns JSON object as dictionary
sampleSolutions = json.load(file)
output = []

# Augment French by BERT
# aug = naw.ContextualWordEmbsAug(model_path='bert-base-multilingual-uncased', aug_p=0.1, action="substitute")
augSubstitute = naw.ContextualWordEmbsAug(model_path='bert-base-german-cased', action="substitute", device="cuda")
augInsert = naw.ContextualWordEmbsAug(model_path='bert-base-german-cased', action="insert", device="cuda")

start = timeit.default_timer()

for key in sampleSolutions:
    text = sampleSolutions[key]
    textsWithSubstitution = augSubstitute.augment(text, 80)
    add_to_output(textsWithSubstitution, key)

    textsWithInsert = augInsert.augment(text, 80)
    add_to_output(textsWithInsert, key)

with open("../assets/text_cat_data.json", "w", encoding="utf-8") as file:
    json.dump(output, file, ensure_ascii=False, indent=4)

end = timeit.default_timer()

print('Datengenerierung Beendet - Laufzeit:', end-start, 'Sekunden')
# Closing file
file.close()

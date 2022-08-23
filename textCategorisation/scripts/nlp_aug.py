import json
import random
import timeit
import nlpaug.augmenter.word as naw

def set_category(category: str):
    output = {}
    categories = ["Rollenunklarheit", "Informationsprobleme", "Variabilität", "Tätigkeitsspielraum", "Zeitdruck", "Arbeitsunterbrechungen", "Soziale Stressoren", "Feedback/Anerkennung", "Soziale Unterstützung"]
    category = category[2:] # remove e.g. 2/
    for cat in categories:
        if cat == category:
            output[cat] = 1.0
        else:
            output[cat] = 0.0
    output['Unbekannt'] = 0.0
    return output

def add_to_output(texts: [str], category: str):
    for text in texts:
        line = {'text': text, 'cats': set_category(category)}
        output.append(line)

def augument_texts(aug_p: float):
    augSubstitute = naw.ContextualWordEmbsAug(model_path='bert-base-german-cased', aug_p=aug_p, action="substitute", device="cuda")
    augInsert = naw.ContextualWordEmbsAug(model_path='bert-base-german-cased', aug_p=aug_p, action="insert", device="cuda")

    for key in sampleTexts:
        text = sampleTexts[key]
        print(key, text)
        textsWithSubstitution = augSubstitute.augment(text, 40)
        add_to_output(textsWithSubstitution, key)

        textsWithInsert = augInsert.augment(text, 40)
        add_to_output(textsWithInsert, key)


# Opening JSON file
file = open('../assets/sample_texts_textcat.json', encoding='utf-8')
# returns JSON object as dictionary
sampleTexts = json.load(file)
file.close()

output = []
start = timeit.default_timer()

augument_texts(0.3)
now = timeit.default_timer()
print(len(output), 'Datasets generated - runtime:', (now-start)/60, 'minutes')

#Add texts with cat = Unbekannt
fileUnknown= open('../assets/cat_unknown.json', encoding='utf-8')
examplesUnknown = json.load(fileUnknown)
for example in examplesUnknown:
    output.append(example)
fileUnknown.close()

with open('../assets/text_cat_data.json', "w", encoding="utf-8") as file:
    json.dump(output, file, ensure_ascii=False, indent=4)

print(len(examplesUnknown), 'Datasets of cateory "Unbekannt" have been added')
file.close()


#####Splitt Data in dev and train ######
file = open('../assets/text_cat_data.json', encoding='utf-8')
# returns JSON object as dictionary
augumentedTexts = json.load(file)

#shuffle texts
random.shuffle(augumentedTexts)

train = []
dev = []

for i in range(len(augumentedTexts)):
    if i%5 == 0: #20% dev
        dev.append(augumentedTexts[i])
    else: #80% test
        train.append(augumentedTexts[i])

with open("../assets/dev.json", "w", encoding="utf-8") as file:
    json.dump(dev, file, ensure_ascii=False, indent=4)
with open("../assets/train.json", "w", encoding="utf-8") as file:
    json.dump(train, file, ensure_ascii=False, indent=4)

print(len(dev), 'Test- and', len(train), 'Trainingdata have been created')
file.close()


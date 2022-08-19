import json
import random

# Opening JSON file
file = open('../assets/generated/train/output.json', encoding='utf-8')

entitiesWithArticle = ['die Produkt-Nummer', 'der Prozessor', 'der Arbeitsspeicher', 'der Preis', 'das Modell', 'die Auflösung', 'die Größe', 'die Diagonale', 'die Farbe']

# returns JSON object as a dictionary
data = json.load(file)

commonExamples = data['rasa_nlu_data']['common_examples']
output = []

### Transform entries from ####
#{"entities": [{ "end": 36, "entity": "monitor_detail", "start": 27, "value": "der Preis"},
#              {"end": 52, "entity": "MONITOR", "start": 41, "value": "Lightmonger"}],
# "intent": "frage_nach_product_detail", "text": "Guten Morgen, wie ist denn der Preis vom Lightmonger?"},
### to ###
#["wie viele Seiten pro Minute schafft der Shardware?", {"entities": [[10, 27, "PROPERTY"], [ 40, 49, "DRUCKER"]]}],
for example in commonExamples:
    entry = []
    entities = {}
    entityList = []
    reducedIndex = 0

    #Bring entities in the needed form
    for entity in example['entities']:
        if not entity['entity'] == 'DRUCKER' and not entity['entity'] == 'PC' and not entity['entity'] == 'MONITOR':
            entity['entity'] = 'PROPERTY'

        # fix start/end for Properties with ö, ß or articles
        if entity['entity'] == 'PROPERTY':
            if 'ö' in example['text'][entity['start']:entity['end']]: #fix start/end-index for die Auflöung und die Größe
                entity['end'] -= 1
                reducedIndex += 1
            if 'ß' in example['text'][entity['start']:entity['end']]:
                    entity['end'] -= 1
                    reducedIndex += 1
            if example['text'][entity['start']:entity['end']] in entitiesWithArticle: # remove article from entity
                entity['start'] += 4
        elif reducedIndex > 0:
            entity['start'] -= reducedIndex
            entity['end'] -= reducedIndex
            reducedIndex = 0
        entityList.append([entity['start'], entity['end'], entity['entity']])

    entities['entities'] = entityList
    entry.append(example['text'])
    entry.append(entities)
    print(entry)

    output.append(entry)

#save formatted data
with open('../assets/generated/train/data-fixed.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)

# Closing file
file.close()


#####Splitt Data in dev and train
file = open('../assets/generated/train/data-fixed.json', encoding='utf-8')
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

# Closing file
file.close()

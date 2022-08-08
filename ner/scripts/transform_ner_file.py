import json
import random

# Opening JSON file
file = open('../assets/generated_output.jsonl', encoding='utf-8')

entitiesWithArticle = ['die Produkt-Nummer', 'der Prozessor', 'der Arbeitsspeicher', 'der Preis', 'das Modell', 'die Auflösung', 'die Größe', 'die Diagonale', 'die Farbe']

# returns JSON object as a dictionary
data = json.load(file)

# Iterating through the json list
count = 0
out = data
for entry in data:
    text = entry[1]
    entry[1]=entry[0]
    entry[0]=text
    reducedIndex = 0
    for entity in entry[1]['entities']:
       # bring entities in the needed order
        end = entity[0]
        entity[0] = entity[2] #start
        entity[2] = entity[1] #type
        entity[1] = end #end

        if entity[2] == 'PROPERTY':
           if 'ö' in text[entity[0]:entity[1]]: #fix start/end-index for die Auflöung und die Größe
                entity[1] -= 1
                reducedIndex += 1
                if 'ß' in text[entity[0]:entity[1]]:
                    entity[1] -= 1
                    reducedIndex += 1
                if 'die' in text[entity[0]:entity[1]]:
                    entity[0] += 4
           if text[entity[0]:entity[1]] in entitiesWithArticle: # remove article from entity
                entity[0] += 4
        elif reducedIndex > 0:
            entity[0] -= reducedIndex
            entity[1] -= reducedIndex
            reducedIndex = 0
        print(text[entity[0]:entity[1]])

    out[count]= entry

    count += 1

with open('../assets/generated_data-fixed.jsonl', 'w', encoding='utf-8') as file:
    json.dump(out, file, ensure_ascii=False, indent=4)

# Closing file
file.close()


#####Splitt Data in dev and train
file = open('../assets/generated_data-fixed.jsonl', encoding='utf-8')
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

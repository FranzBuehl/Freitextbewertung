import spacy

nlp = spacy.load("packages/de_ner_demo-0.0.0/de_ner_demo/de_ner_demo-0.0.0")

doc= nlp("Hallo Frank, kannst du mir beantworten welchen Arbeitsspeicher der Softween eigentlich hat?")

for ent in doc.ents:
    print(ent, ent.label_)

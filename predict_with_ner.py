from numbers import Number

import spacy
import pandas as pd
from random import randint

nlp = spacy.load('packages/de_ner_demo-0.0.0/de_ner_demo/de_ner_demo-0.0.0')

doc = nlp('Hallo Frank, welchen Arbeitsspeicher hat der Deskclix Techbox?')


for ent in doc.ents:
    print(ent.text, ent.label_)

# Ermittle Property, nach der gefragt wurde
def get_requested_property(ents):
    pcs, monitors, printer = read_product_lib()
    properties = [ent for ent in ents if 'PROPERTY' == ent.label_]
    products = [ent for ent in ents if 'PROPERTY' != ent.label_]

    searchedProduct = ''
    productLib = pcs
    # Verwende das erste erkannte Produkt, das in der Bibliothek ist
    for product in products:
        if 'MONITOR' == product.label_:
            productLib = monitors
        elif 'DRUCKER' == product.label_:
            productLib = printer

        productIndex = get_product_index(productLib, product.text)
        if productIndex >= 0:
            searchedProduct = productLib.iloc[productIndex]
            break

    if len(searchedProduct):
        return get_searched_property(searchedProduct, properties)

def create_chat_response(property, answer=''):
    answerTexts, feedbackTexts = read_chat_texts()
    print(answerTexts.iloc[:, 3])
    #Gibt es eine Antwort vom Spieler
    if len(answer):
        if is_answer_correct(answer, property):
            return create_response_text(feedbackTexts.iloc[:, 1], 7)
        else:
            return create_response_text(feedbackTexts.iloc[:, 0], 7)
    else:
        if property:
            answerText = create_response_text(answerTexts, 4, 2)
            answerText = str(answerText).replace('<Experten-Info>', str(property))
            return answerText
        else:
            return create_response_text(answerTexts.iloc[:, 3], 4)

def is_answer_correct(answer, property):
    return str(property) in str(answer)

def create_response_text(availableTexts, maxRow, maxCol=0):
    row = randint(0, maxRow)
    column = randint(0, maxCol)

    if maxCol > 0:
        text = availableTexts.iloc[row, column]
    else:
        text = availableTexts.loc[row]

    # text Manche Spalten haben mehr Zeilen als andere.
    # Deshalb muss evtl. neu gewürfelt werden, wenn kein Text vorhanden ist
    if isinstance(text, Number):
        return create_response_text(availableTexts, maxRow, maxCol)
    else:
        return text

# TODO muss später über eine Schnittstelle eingelesen werden
def read_product_lib():
    dict_df = pd.read_excel('assets/product_lib.xlsx',
                            sheet_name=['Bibliothek - PCs', 'Bibliothek - Monitore', 'Bibliothek - Drucker'],
                            header=1,
                            usecols='B:F')
    return [dict_df.get('Bibliothek - PCs'), dict_df.get('Bibliothek - Monitore'), dict_df.get('Bibliothek - Drucker')]

def read_chat_texts():
    #Antwort-Texte zu einer Frage
    answers_df = pd.read_excel('assets/chat_texts.xlsx',
                            header=2,
                            usecols='G:J')
    #Texte zur Rückmeldung auf eine Antwort
    responses_df = pd.read_excel('assets/chat_texts.xlsx',
                            header=2,
                            usecols='O:P')
    return [answers_df, responses_df]


def get_product_index(lib, productName):
    index = 0
    for modell in lib['Modell']:
        if modell == productName:
            return index
        index += 1
    return -1

#Gibt die erste erkannte Property zurück, die das gegebene Produkt hat
def get_searched_property(product, properties):
    propertyNames = product.keys()
    for property in properties:
        for propertyName in propertyNames:
            if property.text in propertyName:
                searchedProperty = product[propertyName]
                return addUnit(searchedProperty, propertyName)

def addUnit(property, propertyName):
    if 'Preis' == propertyName:
        return str(property) + ' €'
    elif 'Arbeitsspeicher (GB)' == propertyName:
        return str(property) + ' GB'
    elif 'Größe (Diagonale)' == propertyName:
        return str(property) + ' Zoll'
    else:
        return property

property = get_requested_property(doc.ents)
print(property)
print(create_chat_response(property, "1238 GB glaube ich"))

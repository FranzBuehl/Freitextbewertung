from numbers import Number
import spacy
import pandas as pd
from random import randint

class ChatService:
    def handle_chat_request(self, question, answer=''):
        nlp = spacy.load('ner/packages/de_ner-0.0.0/de_ner/de_ner-0.0.0')
        doc = nlp(question)
        property = self.get_requested_property(doc.ents)
        return self.create_chat_response(property, answer)

    # Ermittle Property, nach der gefragt wurde
    def get_requested_property(self, ents):
        pcs, monitors, printer = self.read_product_lib()
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

            productIndex = self.get_product_index(productLib, product.text)
            if productIndex >= 0:
                searchedProduct = productLib.iloc[productIndex]
                break

        if len(searchedProduct):
            return self.get_searched_property(searchedProduct, properties)

    def create_chat_response(self, property, answer):
        answerTexts, feedbackTexts = self.read_chat_texts()
        #Gibt es eine Antwort vom Spieler?
        if len(answer):
            if self.is_answer_correct(answer, property):
                return [self.create_response_text(feedbackTexts.iloc[:, 1], 7), True]
            else:
                return [self.create_response_text(feedbackTexts.iloc[:, 0], 7), False]
        else:
            if property: #Gibt es die gesuchte Property?
                answerText = self.create_response_text(answerTexts, 4, 2)
                answerText = str(answerText).replace('<Experten-Info>', str(property))
                return [answerText, True]
            else:
                return [self.create_response_text(answerTexts.iloc[:, 3], 4), False]

    def is_answer_correct(self, answer, property):
        return str(property) in str(answer)

    def create_response_text(self, availableTexts, maxRow, maxCol=0):
        row = randint(0, maxRow)
        column = randint(0, maxCol)

        if maxCol > 0:
            text = availableTexts.iloc[row, column]
        else:
            text = availableTexts.loc[row]

        # text Manche Spalten haben mehr Zeilen als andere.
        # Deshalb muss evtl. neu gewürfelt werden, wenn kein Text vorhanden ist
        if isinstance(text, Number):
            return self.create_response_text(availableTexts, maxRow, maxCol)
        else:
            return text

    # TODO muss später über eine Schnittstelle eingelesen werden
    def read_product_lib(self):
        dict_df = pd.read_excel('assets/product_lib.xlsx',
                                sheet_name=['Bibliothek - PCs', 'Bibliothek - Monitore', 'Bibliothek - Drucker'],
                                header=1,
                                usecols='B:F')
        return [dict_df.get('Bibliothek - PCs'), dict_df.get('Bibliothek - Monitore'), dict_df.get('Bibliothek - Drucker')]

    def read_chat_texts(self):
        #Antwort-Texte zu einer Frage
        answers_df = pd.read_excel('assets/chat_texts.xlsx',
                                header=2,
                                usecols='G:J')
        #Texte zur Rückmeldung auf eine Antwort
        responses_df = pd.read_excel('assets/chat_texts.xlsx',
                                header=2,
                                usecols='O:P')
        return [answers_df, responses_df]


    def get_product_index(self, lib, productName):
        index = 0
        for modell in lib['Modell']:
            if modell == productName:
                return index
            index += 1
        return -1

    #Gibt die erste erkannte Property zurück, die das gegebene Produkt hat
    def get_searched_property(self, product, properties):
        propertyNames = product.keys()
        for property in properties:
            for propertyName in propertyNames:
                if property.text in propertyName:
                    searchedProperty = product[propertyName]
                    return self.addUnit(searchedProperty, propertyName)

    def addUnit(self, property, propertyName):
        if 'Preis' == propertyName:
            return str(property) + ' €'
        elif 'Arbeitsspeicher (GB)' == propertyName:
            return str(property) + ' GB'
        elif 'Größe (Diagonale)' == propertyName:
            return str(property) + ' Zoll'
        else:
            return property




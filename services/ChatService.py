from numbers import Number
import spacy
import pandas as pd
from random import randint

class ChatService:
    def handle_chat_request(self, question, answer=''):
        nlp = spacy.load('ner/training/model-best')
        doc = nlp(question)
        property = self.get_requested_property(doc.ents)
        return self.create_chat_response(property, answer)

    # Find property that was asked about
    def get_requested_property(self, ents):
        pcs, monitors, printer = self.read_product_lib()
        properties = [ent for ent in ents if 'PROPERTY' == ent.label_]
        products = [ent for ent in ents if 'PROPERTY' != ent.label_]

        searchedProduct = ''
        productLib = pcs

        # Use the first recognized product that is in the library
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
        #Is there an answer from the player?
        if len(answer):
            if self.is_answer_correct(answer, property):
                return True
            else:
                return False
        else:
            if property: #Did we find a property?
                return [property, True]
            else:
                return [None, False]

    def is_answer_correct(self, answer, property):
        return str(property) in str(answer)

    # TODO must be read later via an API
    def read_product_lib(self):
        dict_df = pd.read_excel('assets/product_lib.xlsx',
                                sheet_name=['Bibliothek - PCs', 'Bibliothek - Monitore', 'Bibliothek - Drucker'],
                                header=1,
                                usecols='B:F')
        return [dict_df.get('Bibliothek - PCs'), dict_df.get('Bibliothek - Monitore'), dict_df.get('Bibliothek - Drucker')]

    def get_product_index(self, lib, productName):
        index = 0
        for modell in lib['Modell']:
            if modell == productName:
                return index
            index += 1
        return -1

    #Returns the first recognized property that the given product has
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




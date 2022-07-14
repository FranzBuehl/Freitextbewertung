import spacy


class ExplainService:
    def explain_simularity(self):
        nlp = spacy.load('./textCategorisation/training/model-best')
        doc = nlp('Es sollte nur einen sinnvoll benannten Hauptordner im Dateiverzeichnis geben und nicht mehrere, sinnlos benannte Unterverzeichnisse')
        print(doc.cats)
        # property = self.get_requested_property(doc.ents)
        # return self.create_chat_response(property, answer)


service = ExplainService()
service.explain_simularity()

import shap
import spacy

textcat_model = spacy.load('textCategorisation/training/model-best')
tokenizer = spacy.tokenizer.Tokenizer(textcat_model.vocab)
classes = list(textcat_model.get_pipe("textcat").labels)

class ExplainService:

    # Define a function to predictcd
    def predict(self, texts):
        # convert texts to bare strings
        texts = [str(text) for text in texts]
        results = []
        for doc in textcat_model.pipe(texts):
            # results.append([{'label': cat, 'score': doc.cats[cat]} for cat in doc.cats])
            results.append([doc.cats[cat] for cat in classes])
        return results
    
    # Create a function to create a transformers-like tokenizer to match shap's expectations
    def tok_wrapper(self, text, return_offsets_mapping=False):
        doc = tokenizer(text)
        out = {"input_ids": [tok.norm for tok in doc]}
        if return_offsets_mapping:
            out["offset_mapping"] = [(tok.idx, tok.idx + len(tok)) for tok in doc]
        return out

# Create the Shap Explainer
# - predict is the "model" function, adapted to a transformers-like model
# - masker is the masker used by shap, which relies on a transformers-like tokenizer
# - algorithm is set to permutation, which is the one used for transformers models
# - output_names are the classes (although it is not propagated to the permutation explainer currently, which is why plots do not have the labels)
# - max_evals is set to a high number to reduce the probability of cases where the explainer fails because there are too many tokens

service = ExplainService()

explainer = shap.Explainer(
        service.predict,
        masker=shap.maskers.Text(service.tok_wrapper),
        algorithm="permutation",
        output_names=classes,
        max_evals=1500)

shap_values = explainer(['Die Kriterien für korrekte oder falsche Antworten müssen eindeutig benannt werden. Eine Banane ist kein Gummiboot'])
shap_values.output_names = classes
# shap.plots.text(shap_values)

html = shap.plots.text(shap_values, display=False)
with open('html_file.html', 'w') as f:
    f.write(html)
# service.explain_simularity()

# explainer = shap.Explainer(textcat_model)
# shap_values = explainer(['Es sollte nur einen sinnvoll benannten Hauptordner im Dateiverzeichnis geben und nicht mehrere, sinnlos benannte Unterverzeichnisse'])
# print(shap_values.values)
# shap.plots.text(shap_values)

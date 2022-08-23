import shap
import spacy

from entities import Exercise

textcat_model = spacy.load('textCategorisation/training/model-best')
tokenizer = spacy.tokenizer.Tokenizer(textcat_model.vocab)
categories = list(textcat_model.get_pipe("textcat").labels)

class ExplainService:

    # Define a function to predict the category
    def predict(self, texts):
        # convert texts to bare strings
        texts = [str(text) for text in texts]
        results = []
        for doc in textcat_model.pipe(texts):
            results.append([doc.cats[cat] for cat in categories])
        return results
    
    # Create a function to create a transformers-like tokenizer
    # to match shap's expectations
    def tok_wrapper(self, text, return_offsets_mapping=False):
        doc = tokenizer(text)
        out = {"input_ids": [tok.norm for tok in doc]}
        if return_offsets_mapping:
            out["offset_mapping"] = [(tok.idx, tok.idx + len(tok)) for tok in doc]
        return out

    def explain(self, quiz: list[Exercise], explanationPath: str):
        texts = [exercise.solution for exercise in quiz if exercise.has_sample_solution()]

        # Create the Shap Explainer
        explainer = shap.Explainer(
        self.predict,
        masker=shap.maskers.Text(self.tok_wrapper),
        algorithm="permutation",
        output_names=categories,
        max_evals=1500)

        shap_values = explainer(texts)
        shap_values.output_names = categories

        #create and save explanation
        html = shap.plots.text(shap_values, display=False)
        with open(explanationPath, 'w') as f:
            f.write(html)




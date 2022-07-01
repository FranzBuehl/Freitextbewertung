import spacy
import pandas as pd
import random
from spacy.util import minibatch, compounding
#import shap
from thinc.api import set_gpu_allocator, require_gpu

# Use the GPU, with memory allocations directed via PyTorch.
# This prevents out-of-memory errors that would otherwise occur from competing
# memory pools.
# set_gpu_allocator("pytorch")
require_gpu() #distiluse-base-multilingual-cased-v1

# load one of the models listed at https://github.com/MartinoMensio/spacy-sentence-bert/
nlp = spacy.load('de_dep_news_trf')
#nlp.add_pipe('sentence_bert', config={'model_name': 'xx_stsb_xlm_r_multilingual'}) #'T-Systems-onsite/cross-en-de-roberta-sentence-transformer'})

doc1 = nlp("Es muss klar sein, wer wann was wie machen soll. Die Ziele des Computershops müssen klar werden. Am Anfang muss beschrieben werden, wie das Spiel abläuft und worum es genau geht. Es muss klar benannt werden, wofür es im Spiel Punkte gibt und wofür nicht. Auch muss spezifiziert werden, wer Weisungsbefugnisse hat und wer nicht")
doc2 = nlp("Es sollte erklärt werden, was getan werden muss, was die Ziele des Shops sind und wie der Ablauf des Spiels ist.")
#doc2 = nlp("Man muss genau wissen, worum es beim Spiel oder den Aufgaben geht und was wie gewertet wird. Dazu wird am Anfang eine Beschreibung oder Einleitungen benötigt, die die Ziele der Aufgaben deutlich machen.")

#print(doc1.ents, len(doc1.ents))
#print(doc1.tensor)
#shap_values = explainer(doc1.tensor)

x =0;
for sent1 in doc1.sents:
  x+= 1
  y=0;
  for sent2 in doc2.sents:
    y += 1
    print(sent1.similarity(sent2), x, y)
print(doc1.similarity(doc2))

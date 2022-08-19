<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Predicts to which of the questions an answer belongs (Text Classification)

This project uses [spaCy](https://spacy.io) with data that is generated with nlpaug (nlp_aug.py) to train a **text classifier** to predict to which of the questions of the final Quiz an answer belongs. The pipeline uses the component `textcat_multilabel` in order to train the classifier.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's binary format |
| `train` | Train a text classification model |
| `evaluate` | Evaluate the model and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. 

| File                                                                                                                       | Source | Description                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`assets/train.json`]| Local | JSONL-formatted training data (80%) generated with nlpaug and the script scripts/nlp_aug.py. Manual created data for the category 'Unbekannt' from assets/cat_unknown.json are also added by the script. |
| [`assets/dev.jsonl`] | Local | JSONL-formatted test data generated (20%) with nlpaug and the script scripts/nlp_aug.py. Manual created data for the category 'Unbekannt' from assets/cat_unknown.json are also added by the script.     |

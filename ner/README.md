<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# NER Project to detect Properties in Chat-Texts 

## 📋 project.yml

The [`project.yml`](../project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `convert` | Convert the data to spaCy's binary format |
| `train` | Train the NER model |
| `evaluate` | Evaluate the model and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description                                       |
| --- | --- |---------------------------------------------------|
| [`assets/train.json`](assets/ner/train.json) | Local | Generated train Data from data_template.txt       |
| [`assets/dev.json`](assets/ner/dev.json) | Local | Generated development Data from data_template.txt |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

# This is the Prototype for the PAGEL Text Analytics-Tool  

## To initial use the Project:

Make sure you have installed Python and install pip or an other Package installer for Python
`py -m pip install --upgrade pip`

Get a cuda driver for your hardware and the matching cupy-cuda to use your GPU
`https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html`
`https://cupy.dev/`

Install Spacy
`pip install -U spacy`

Install the other dependencies and start the application
`spacy project run start`

Use [FastAPI](https://fastapi.tiangolo.com/) to host the application. To explore the REST API interactively, navigate to `http://127.0.0.1:5000/docs` in your browser. See the examples for how to query the API using Python or JavaScript.

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
| `install` | Install dependencies and download models |
| `serve` | Serve the models via a FastAPI REST API using the given host and port |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `start` | `install` &rarr; `serve` |


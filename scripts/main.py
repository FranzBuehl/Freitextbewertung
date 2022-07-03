from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat_service import handle_chat_request

# Set up the FastAPI app and define the endpoints

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

class EvaluationRequestModel(BaseModel):
    question: str
    answer: str

class AnswerRequestModel(BaseModel):
    question: str

class ResponseModel(BaseModel):
    response: str


@app.post("/chat/evaluation", summary="Evaluate Chat-Answer", response_model=ResponseModel)
def process_articles(query: EvaluationRequestModel):
    """Ermittelt die passende Lösung für eine Frage und vergleicht sie mit der gegebenen Antwort,
    um eine passende Rückmeldung zu geben
    """
    response = handle_chat_request(query.question, query.answer)
    return {"response": response}

@app.post("/chat/answer", summary="Answers Chat-Question", response_model=ResponseModel)
def process_articles(query: AnswerRequestModel):
    """Erzeugt eine Antwort für eine Frage aus dem Chat
    """
    response = handle_chat_request(query.question)
    return {"response": response}

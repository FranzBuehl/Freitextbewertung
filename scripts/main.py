from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ChatService import ChatService
from assessment_service import assess
from entities.ChatRequestModel import ChatRequestModel
from entities.ChatResponseModel import ChatResponseModel
from entities.QuizRequestModel import QuizRequestModel

# Set up the FastAPI app and define the endpoints
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.post("/chat/evaluation", summary="Evaluate Chat-Answer", response_model=ChatResponseModel)
def evaluate_chat_answer(query: ChatRequestModel):
    """Ermittelt die passende Lösung für eine Frage und vergleicht sie mit der gegebenen Antwort,
    um eine passende Rückmeldung zu geben
    """
    service = ChatService()
    response = service.handle_chat_request(query.question, query.answer)
    return {"response": response}

@app.post("/chat/answer", summary="Answers Chat-Question", response_model=ChatResponseModel)
def answer_chat_question(query: ChatRequestModel):
    """Erzeugt eine Antwort für eine Frage aus dem Chat
    """
    service = ChatService()
    response = service.handle_chat_request(query.question)
    return {"response": response}

@app.post("/quiz/assessment")
def assess_quiz(request: QuizRequestModel):
    return assess(request)


# @app.post("/quiz/update")

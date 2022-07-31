from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ChatService import ChatService
from AssessmentService import AssessmentService
from entities.ChatRequestModel import ChatRequestModel
from entities.ChatResponseModel import ChatResponseModel
from entities.QuizRequestModel import QuizRequestModel

# Set up the FastAPI app and define the endpoints
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.post("/chat/evaluation", summary="Evaluate Chat-Answer", response_model=ChatResponseModel)
def evaluate_chat_answer(query: ChatRequestModel):
    """Evaluates if a Chat-Question is answered correct
    """
    service = ChatService()
    success = service.handle_chat_request(query.question, query.answer)
    return {"success": success}

@app.post("/chat/answer", summary="Answers Chat-Question", response_model=ChatResponseModel)
def answer_chat_question(query: ChatRequestModel):
    """Extracts the searched Property from the product_lib and returns it
    """
    service = ChatService()
    response, success = service.handle_chat_request(query.question)
    return {"response": response, "success": success}

@app.post("/quiz/assessment", summary="Assesses the quiz answers and assigns a competency")
def assess_quiz(request: QuizRequestModel):
    """Rates the Quiz Answers depending on keywords and semantic similarity to the sample solution.
    Saves the result with the resulting competence."""
    service = AssessmentService()
    service.assess(request)


# @app.post("/quiz/update")

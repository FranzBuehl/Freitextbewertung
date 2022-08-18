from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from entities.ChatEvaluationRequestModel import ChatEvaluationRequestModel
from entities.ChatAnswerRequestModel import ChatAnswerRequestModel
from entities.ChatEvaluationResponseModel import ChatEvaluationResponseModel
from entities.ChatAnswerResponseModel import ChatAnswerResponseModel
from services.ChatService import ChatService
from services.QuizService import QuizService
from services.ExplainService import ExplainService
from entities.QuizRequestModel import QuizRequestModel

# Set up the FastAPI app and define the endpoints
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.post("/1.0/chat/evaluation", summary="Evaluate Chat-Answer", response_model=ChatEvaluationResponseModel)
def evaluate_chat_answer(query: ChatEvaluationRequestModel):
    """Evaluates if a Chat-Question is answered correct
    """
    service = ChatService()
    success = service.handle_chat_request(query.question, query.answer)

    return {"success": success}

@app.post("/1.0/chat/answer", summary="Answers Chat-Question", response_model=ChatAnswerResponseModel)
def answer_chat_question(query: ChatAnswerRequestModel):
    """Extracts the searched Property from the product_lib and returns it
    """
    service = ChatService()
    response, success = service.handle_chat_request(query.question)

    return {"response": response, "success": success}

@app.post("/1.0/quiz/assessment", summary="Assesses the quiz answers and assigns a competency")
def assess_quiz(request: QuizRequestModel):
    """Rates the Quiz Answers depending on keywords and semantic similarity to the sample solution.
    Saves the result with the resulting competence and an explanation."""
    quizService = QuizService()
    assessment = quizService.rate(request)

    explainService = ExplainService()
    explainService.explain(request.quiz, assessment.explanationPath)


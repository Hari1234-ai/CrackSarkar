from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db.base import Question
from pydantic import BaseModel
from typing import Optional, Dict, Any

router = APIRouter()

class QuestionSchema(BaseModel):
    id: str
    topic_id: str
    type: str # mcq, true_false, matching
    question_text: str
    options: Optional[Any] = None
    correct_answer: str
    explanation: Optional[str] = None

    class Config:
        from_attributes = True

@router.get("/questions/{topic_id}", response_model=List[QuestionSchema])
def get_topic_questions(topic_id: str, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.topic_id == topic_id).all()
    return questions

@router.get("/random", response_model=List[QuestionSchema])
def get_random_questions(limit: int = 5, db: Session = Depends(get_db)):
    from sqlalchemy.sql.expression import func
    questions = db.query(Question).order_by(func.random()).limit(limit).all()
    return questions

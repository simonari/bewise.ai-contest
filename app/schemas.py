from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Question(Base):
    id: int
    question: str
    answer: str
    created_at: datetime


class QuestionResponse(Base):
    question: str

from typing import TYPE_CHECKING
from sqlalchemy import select

from . import database
from . import models
from . import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_tables():
    return models.Base.metadata.create_all(database.engine)


async def add_questions(questions: list[schemas.Question],
                        db: "Session") -> None:
    questions = [models.Question(**q.model_dump()) for q in questions]

    db.add_all(questions)
    db.commit()


async def check_ids(question_ids: list[int], db: "Session") -> list[int]:
    query = select(models.Question.id).filter(models.Question.id.in_(question_ids))
    result = db.execute(query)

    result = [q[0] for q in result]

    return result


async def last_question(db: "Session") -> schemas.QuestionResponse:
    query = select(models.Question).order_by(models.Question.saved_at.desc())
    result = db.execute(query).first()[0]

    return schemas.QuestionResponse(question=result.question)

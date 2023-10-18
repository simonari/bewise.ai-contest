import fastapi
from fastapi import FastAPI
import sqlalchemy.orm as orm
from .services import DataBaseManager
from .ext import quiz

app = FastAPI()
db_manager = DataBaseManager()

MAX_ATTEMPTS = 5


@app.post("/{questions_num}")
async def retrieve_questions(questions_num: int,
                             db: orm.Session = fastapi.Depends(db_manager.get_db)):
    last_question = await db_manager.last_question(db)

    attempt = 0
    remaining = questions_num
    while attempt < MAX_ATTEMPTS and remaining > 0:
        questions = quiz.get_questions(remaining)

        ids = [q.id for q in questions]
        ids_in_db = await db_manager.check_ids(ids, db)
        ids_not_in_db = [i for i in ids if i not in ids_in_db]

        to_add = []

        for q in questions:
            if q.id in ids_in_db:
                continue

            to_add.append(q)

        remaining = len(ids) - len(ids_not_in_db)
        attempt += 1

        await db_manager.add_questions(to_add, db)

    return last_question

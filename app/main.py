import fastapi
from fastapi import FastAPI
import sqlalchemy.orm as orm
from . import schemas
from . import services
from .ext import quiz

app = FastAPI()
services.add_tables()

MAX_ATTEMPTS = 5


@app.post("/{questions_num}")
async def retrieve_questions(questions_num: int,
                             db: orm.Session = fastapi.Depends(services.get_db)):
    last_question = await services.last_question(db)

    attempt = 0
    remaining = questions_num
    while attempt < MAX_ATTEMPTS and remaining > 0:
        questions = quiz.get_questions(remaining)

        ids = [q.id for q in questions]
        ids_in_db = await services.check_ids(ids, db)
        ids_not_in_db = [i for i in ids if i not in ids_in_db]

        to_add = []

        for q in questions:
            if q.id in ids_in_db:
                continue

            to_add.append(q)

        remaining = len(ids) - len(ids_not_in_db)
        attempt += 1

        await services.add_questions(to_add, db)

    return last_question


@app.get("/{questions_num}")
async def show_last():
    pass

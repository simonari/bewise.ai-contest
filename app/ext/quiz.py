import requests
import json
from dotenv import load_dotenv
import os
from .. import schemas

load_dotenv()
URL = os.getenv("QUIZ_URL")


def get_questions(n: int) -> list[schemas.Question]:
    response = requests.get(URL, {"count": n})

    questions = json.loads(response.content)

    result = [schemas.Question(id=q["id"],
                               question=q["question"],
                               answer=q["answer"],
                               created_at=q["created_at"])
              for q in questions]

    return result

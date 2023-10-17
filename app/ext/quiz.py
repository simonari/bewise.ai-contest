import requests
from .. import schemas
import json

URL = "https://jservice.io/api/random"


def get_questions(n: int) -> list[schemas.Question]:
    response = requests.get(URL, {"count": n})

    questions = json.loads(response.content)

    result = [schemas.Question(id=q["id"], question=q["question"], answer=q["answer"], created_at=q["created_at"]) for q
              in questions]

    return result

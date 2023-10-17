import db
import models


def add_tables():
    return models.Base.metadata.create_all(db.engine)

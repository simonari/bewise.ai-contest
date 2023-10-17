import sqlalchemy as sql
import sqlalchemy.orm as orm


class Base(orm.DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "questions"

    id = sql.Column(sql.Integer, primary_key=True, index=True)
    question = sql.Column(sql.Text)
    answer = sql.Column(sql.Text)
    created_at = sql.Column(sql.DateTime)

    def __repr__(self) -> str:
        return f"Question No. {self.id}. Q: {self.question}. A: {self.answer}. Was created: {self.created_at}"

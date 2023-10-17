import sqlalchemy as sql
import sqlalchemy.orm as orm
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"

engine = sql.create_engine(DB_URL)

SessionLocal = orm.sessionmaker(bind=engine, autocommit=False, autoflush=False)

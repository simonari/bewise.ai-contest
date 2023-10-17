import sqlalchemy as sql
import sqlalchemy.orm as orm

DB_URL = "postgresql://postgres:postgres@localhost/bewise.ai"

engine = sql.create_engine(DB_URL)

SessionLocal = orm.sessionmaker(bind=engine, autocommit=False, autoflush=False)

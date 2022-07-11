from contextvars import ContextVar
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

USER = os.environ.get('DATABASE_USER', "lucky")
PASSWORD = os.environ.get('DATABASE_PASSWORD', "1234")
HOST = os.environ.get('DATABASE_HOST', "localhost")
PORT = os.environ.get('DATABASE_PORT', 5432)
NAME = os.environ.get('DATABASE_NAME', "crud")

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}")

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()

db_session: ContextVar[Session] = ContextVar("db_session", default=None)


def get_db():
    """get db"""
    if not db_session.get():
        db = SessionLocal()
        db_session.set(db)
        return db
    return db_session.get()

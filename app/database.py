from typing import Any

from sqlalchemy import (
    Column,
    CursorResult,
    Insert,
    Integer,
    Select,
    String,
    Update,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base

from app.configs import settings

engine = create_engine(settings.DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, index=True)


def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)


def execute(query: Insert | Update):
    with engine.connect() as connection:
        result = connection.execute(query)
        connection.commit()

        return result


def fetch_one(query: Select) -> dict[str, Any] | None:
    with engine.connect() as connection:
        cursor: CursorResult = connection.execute(query)
        data = cursor.fetchone()

        return data if data else None


def fetch_all(query: Select) -> list[dict[str, Any]]:
    with engine.connect() as connection:
        cursor: CursorResult = connection.execute(query)
        return [row._asdict() for row in cursor.fetchall()]

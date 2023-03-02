from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import (
    SQL_ENGINE,
    SQL_USER,
    SQL_PASS,
    SQL_HOST,
    SQL_DB,
    SQL_PORT,
)


SQLALCHEMY_DATABASE_URL = (
    f"{SQL_ENGINE}+asyncpg://{SQL_USER}:{SQL_PASS}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

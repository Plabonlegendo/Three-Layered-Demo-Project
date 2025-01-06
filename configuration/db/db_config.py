import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()  # taking environment variables from .env.

DB_BASE_URL = os.environ.get("DB_BASE_URL")
DB_NAME = os.environ.get("DB_NAME")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_SCHEMA = os.environ.get("DB_SCHEMA")

SQLALCHEMY_DATABASE_URL = \
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_BASE_URL}/{DB_NAME}?options=-c search_path={DB_SCHEMA}"


engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       pool_pre_ping=True,
                       pool_size=10,
                       max_overflow=2,
                       pool_recycle=30,
                       connect_args={
                           "keepalives": 5,
                           "keepalives_idle": 3,
                           "keepalives_interval": 3,
                           "keepalives_count": 5,
                       },
                       future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()
UserBase = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
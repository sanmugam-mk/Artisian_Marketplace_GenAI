import os

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base
Base = declarative_base()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
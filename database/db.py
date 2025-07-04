import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

username = os.getenv("USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
domain = os.getenv("DOMAIN")

url = f"postgresql://{username}:{password}@{domain}:5433/{db_name}"

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

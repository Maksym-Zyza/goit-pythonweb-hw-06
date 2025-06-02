import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

username = os.getenv("USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
domain = os.getenv("DOMAIN")

#  f'postgresql://username:password@domain_name:port/database_name'

url = f'postgresql://{username}:{password}@{domain}:5433/{db_name}'

# Create engine and session
engine = create_engine(url, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

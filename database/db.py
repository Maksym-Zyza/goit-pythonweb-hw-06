from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
domain = os.getenv("DOMAIN")

url = f'postgresql://{username}:{password}@{domain}:5433/{db_name}'
engine = create_engine(url, echo=True)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(result.fetchone())
except Exception as e:
    print("Connection error:", e)

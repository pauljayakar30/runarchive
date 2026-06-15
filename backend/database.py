from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///data/runarchive.db"

db_path = os.path.abspath("data/runarchive.db")

print("DATABASE FILE:")
print(db_path)

engine = create_engine(
    f"sqlite:///{db_path}",
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
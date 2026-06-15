from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/runarchive.db"

engine = create_engine(DATABASE_URL)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .get_env import DATABASE_URL

engine = create_engine(DATABASE_URL)

Session = sessionmaker(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """
    Dependency for database session.

    :return: Database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

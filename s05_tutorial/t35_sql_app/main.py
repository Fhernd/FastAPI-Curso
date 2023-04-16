from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create user.

    :param user: User to create
    :param db: Database session.

    :return: Created user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get users.

    :param skip: skip first N users
    :param limit: limit users to N
    :param db: database session

    :return: List of users.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get user by id.

    :param user_id: user ID
    :param db: database session

    :return: User with given ID or None if not found.
    """
    db_user = crud.get_user(db, user_id=user_id)
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create item for user.

    :param user_id: User ID
    :param item: Item to create
    :param db: Database session

    :return: Created item.
    """
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get items.

    :param skip: skip first N items
    :param limit: limit items to N
    :param db: database session

    :return: List of items.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

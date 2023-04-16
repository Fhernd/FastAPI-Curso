from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    """
    Get user by id.

    :param db: database session
    :param user_id: user ID

    :return: User with given ID or None if not found.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Get user by email.

    :param db: database session
    :param email: user email

    :return: User with given email or None if not found.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Get users.

    :param db: database session
    :param skip: skip first N users
    :param limit: limit users to N

    :return: List of users.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Create user.

    :param db: Database session.
    :param user: User to create

    :return: Created user.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Get items.

    :param db: database session
    :param skip: skip first N items
    :param limit: limit items to N

    :return: List of items.
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """
    Create item for user.

    :param db: Database session
    :param item: Item to create
    :param user_id: User ID

    :return: Created item.
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    """
    Get user by id.

    :param db: database session
    :param user_id: user ID
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Get user by email.

    :param db: database session
    :param email: user email
    """
    return db.query(models.User).filter(models.User.email == email).first()

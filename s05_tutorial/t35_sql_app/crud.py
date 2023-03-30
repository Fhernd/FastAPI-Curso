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


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Get users.

    :param db: database session
    :param skip: skip first N users
    :param limit: limit users to N
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

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    """
    Get user by id.

    :param db: database session
    :param user_id: user ID
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

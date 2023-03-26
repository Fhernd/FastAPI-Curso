from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Base class for Item.
    """
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    """
    Class for creating Item.
    """
    pass


class Item(ItemBase):
    """
    Class for Item.
    """
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    """
    Base class for User.
    """
    email: str


class UserCreate(UserBase):
    """
    Class for creating User.
    """
    password: str


class User(UserBase):
    """
    Class for User.
    """
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Ortiz Ordoñez'
    signup_ts: datetime | None = None
    friends: list[int] = []


# Desde el exterior podríamos recibir estos datos:
external_data = {
    'id': 1001, 
    'signup_ts': '2022-10-23 12:20', 
    'friends': [1002, 1003, 1004]
}

user = User(**external_data)
print(user)
print(user.id)

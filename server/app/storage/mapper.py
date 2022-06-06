from abc import ABC, abstractmethod
from ..settings import MAPPER_TYPE, MapperEnum
from ..schemas.user import UserInDB

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

class MapperInterface(ABC):

    @abstractmethod
    def get_user(self, username: str) -> UserInDB | None:
        """Get a user from the database.
        """
        raise NotImplemented


class FakeMapper(MapperInterface):
    def __init__(self, database):
        self._db = database

    def get_user(self, username: str) -> UserInDB | None:
        if username in self._db:
            user_dict = self._db[username]
            return UserInDB(**user_dict)


class EdgeDBMapper(MapperInterface):
    def __init__(self, database):
        self._db = database

    def get_user(self, username: str) -> UserInDB | None:
        if username in self._db:
            user_dict = self._db[username]
            return UserInDB(**user_dict)


def get_default_mapper():
    if MapperEnum.fake == MAPPER_TYPE:
        return FakeMapper(fake_users_db)
    elif MapperEnum.edgedb == MAPPER_TYPE:
        return EdgeDBMapper({})
    raise RuntimeError(f"Unknown mapper type {MAPPER_TYPE}")


MAPPER = get_default_mapper()

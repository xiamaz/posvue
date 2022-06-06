from enum import Enum
from decouple import config

class MapperEnum(str, Enum):
    fake = "fake"
    edgedb = "edgedb"

JWT_SECRET_KEY = config("JWT_SECRET_KEY")
MAPPER_TYPE = config("MAPPER_TYPE")

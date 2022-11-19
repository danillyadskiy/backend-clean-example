from pydantic import BaseModel


class Author(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str
